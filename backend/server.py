import asyncio
import json
import random
from datetime import datetime
from aiohttp import web
import aiohttp_cors
from collections import defaultdict

# Game state
games = {}
player_to_game = {}

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.players = {}  # ws: {name, score, id}
        self.started = False
        self.deck = []
        self.flipped_cards = []
        self.current_player_turn = None
        self.card_positions = {}
        self.matched_cards = set()
        
    def add_player(self, ws, player_name):
        if len(self.players) >= 5:
            return False
        player_id = len(self.players)
        self.players[ws] = {
            'name': player_name,
            'score': 0,
            'id': player_id
        }
        return True
    
    def remove_player(self, ws):
        if ws in self.players:
            del self.players[ws]
    
    def start_game(self):
        if len(self.players) < 2:
            return False
        self.started = True
        # Create deck with pig-themed pairs (14 pairs = 28 cards)
        pig_items = ['🐷', '🐖', '🥓', '🌸', '🎀', '🐽', '💕', '⭐', '🎪', '🎯', '🎨', '🎭', '🎪', '🍎']
        self.deck = pig_items * 2
        random.shuffle(self.deck)
        # Assign turn to first player
        first_ws = list(self.players.keys())[0]
        self.current_player_turn = self.players[first_ws]['id']
        return True
    
    def flip_card(self, player_ws, card_index):
        if not self.started:
            return {'error': 'Game not started'}
        
        player_id = self.players[player_ws]['id']
        if player_id != self.current_player_turn:
            return {'error': 'Not your turn'}
        
        if card_index in self.matched_cards:
            return {'error': 'Card already matched'}
        
        if card_index in self.flipped_cards:
            return {'error': 'Card already flipped'}
        
        if len(self.flipped_cards) >= 3:
            return {'error': 'Too many cards flipped'}
        
        self.flipped_cards.append(card_index)
        card_value = self.deck[card_index]
        
        result = {
            'card_index': card_index,
            'card_value': card_value,
            'flipped_count': len(self.flipped_cards)
        }
        
        # Check if 3 cards match
        if len(self.flipped_cards) == 3:
            cards_values = [self.deck[i] for i in self.flipped_cards]
            if len(set(cards_values)) == 1:  # All three match
                # Point scored!
                self.players[player_ws]['score'] += 1
                for idx in self.flipped_cards:
                    self.matched_cards.add(idx)
                result['match'] = True
                result['scorer'] = player_id
                result['new_score'] = self.players[player_ws]['score']
                
                # Check for winner
                if self.players[player_ws]['score'] >= 7:
                    result['winner'] = player_id
                    result['winner_name'] = self.players[player_ws]['name']
            else:
                result['match'] = False
                # Next player's turn
                player_ids = [p['id'] for p in self.players.values()]
                current_idx = player_ids.index(self.current_player_turn)
                self.current_player_turn = player_ids[(current_idx + 1) % len(player_ids)]
                result['next_turn'] = self.current_player_turn
            
            self.flipped_cards = []
        
        return result

# WebSocket connections
connections = set()

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    connections.add(ws)
    
    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                data = json.loads(msg.data)
                action = data.get('action')
                
                if action == 'create_game':
                    player_name = data.get('name', 'Player')
                    game_id = f"game_{len(games)}_{datetime.now().timestamp()}"
                    game = Game(game_id)
                    game.add_player(ws, player_name)
                    games[game_id] = game
                    player_to_game[ws] = game_id
                    
                    await ws.send_json({
                        'type': 'game_created',
                        'game_id': game_id,
                        'player_id': game.players[ws]['id']
                    })
                
                elif action == 'join_game':
                    game_id = data.get('game_id')
                    player_name = data.get('name', 'Player')
                    
                    if game_id in games:
                        game = games[game_id]
                        if game.add_player(ws, player_name):
                            player_to_game[ws] = game_id
                            
                            # Notify all players
                            players_list = [
                                {'id': p['id'], 'name': p['name'], 'score': p['score']}
                                for p in game.players.values()
                            ]
                            
                            for player_ws in game.players.keys():
                                await player_ws.send_json({
                                    'type': 'player_joined',
                                    'players': players_list,
                                    'your_id': game.players[player_ws]['id']
                                })
                        else:
                            await ws.send_json({'type': 'error', 'message': 'Game full'})
                    else:
                        await ws.send_json({'type': 'error', 'message': 'Game not found'})
                
                elif action == 'start_game':
                    if ws in player_to_game:
                        game_id = player_to_game[ws]
                        game = games[game_id]
                        
                        if game.start_game():
                            # Notify all players
                            for player_ws in game.players.keys():
                                await player_ws.send_json({
                                    'type': 'game_started',
                                    'deck_size': len(game.deck),
                                    'current_turn': game.current_player_turn
                                })
                        else:
                            await ws.send_json({'type': 'error', 'message': 'Need at least 2 players'})
                
                elif action == 'flip_card':
                    if ws in player_to_game:
                        game_id = player_to_game[ws]
                        game = games[game_id]
                        card_index = data.get('card_index')
                        
                        result = game.flip_card(ws, card_index)
                        
                        # Broadcast to all players
                        for player_ws in game.players.keys():
                            await player_ws.send_json({
                                'type': 'card_flipped',
                                **result
                            })
                
                elif action == 'get_state':
                    if ws in player_to_game:
                        game_id = player_to_game[ws]
                        game = games[game_id]
                        
                        players_list = [
                            {'id': p['id'], 'name': p['name'], 'score': p['score']}
                            for p in game.players.values()
                        ]
                        
                        await ws.send_json({
                            'type': 'game_state',
                            'players': players_list,
                            'started': game.started,
                            'current_turn': game.current_player_turn,
                            'matched_cards': list(game.matched_cards),
                            'your_id': game.players[ws]['id']
                        })
            
            elif msg.type == web.WSMsgType.ERROR:
                print(f'WebSocket error: {ws.exception()}')
    
    finally:
        connections.discard(ws)
        if ws in player_to_game:
            game_id = player_to_game[ws]
            if game_id in games:
                game = games[game_id]
                game.remove_player(ws)
                
                # Notify remaining players
                if len(game.players) == 0:
                    del games[game_id]
                else:
                    players_list = [
                        {'id': p['id'], 'name': p['name'], 'score': p['score']}
                        for p in game.players.values()
                    ]
                    for player_ws in game.players.keys():
                        await player_ws.send_json({
                            'type': 'player_left',
                            'players': players_list
                        })
            
            del player_to_game[ws]
    
    return ws

async def index_handler(request):
    return web.FileResponse('/home/claude/incha-porco/frontend/index.html')

app = web.Application()
app.router.add_get('/ws', websocket_handler)
app.router.add_get('/', index_handler)
app.router.add_static('/', '/home/claude/incha-porco/frontend/')

# Configure CORS
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})

for route in list(app.router.routes()):
    cors.add(route)

if __name__ == '__main__':
    print("Starting Incha Porco server on http://0.0.0.0:8080")
    web.run_app(app, host='0.0.0.0', port=8080)
