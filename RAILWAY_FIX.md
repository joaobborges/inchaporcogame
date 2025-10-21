# 🔧 Railway Deployment Troubleshooting

## Your URL: https://web-production-00b7c.up.railway.app/

Let me help you fix this! Here are the most common issues and solutions:

---

## Issue 1: Server Not Binding to Railway's PORT ✅ MOST LIKELY

Railway assigns a dynamic PORT. Your server needs to use it.

### Fix:

Update your `server.py` - Find this line near the bottom:

```python
# FIND THIS:
with socketserver.TCPServer(("0.0.0.0", PORT), GameHandler) as httpd:
```

Make sure at the TOP of your file you have:

```python
import os
PORT = int(os.environ.get('PORT', 8080))
```

**Complete Fixed Version:**

Replace the ENTIRE last section of `server.py` with:

```python
import os

# Use Railway's dynamic PORT
PORT = int(os.environ.get('PORT', 8080))

print(f"Starting Incha Porco server on http://0.0.0.0:{PORT}")
print(f"Access the game at: http://0.0.0.0:{PORT}/")

with socketserver.TCPServer(("0.0.0.0", PORT), GameHandler) as httpd:
    httpd.serve_forever()
```

---

## Issue 2: Missing or Incorrect Procfile

### Check Your Procfile:

Create/update `Procfile` (no extension!) with exactly this:

```
web: python3 server.py
```

**Important:** 
- Must be named exactly `Procfile` (capital P, no extension)
- Must contain exactly that one line
- No extra spaces or characters

---

## Issue 3: Python Version Mismatch

### Create `runtime.txt`:

```
python-3.11.0
```

This tells Railway which Python version to use.

---

## Issue 4: Frontend Path Issues

In your `server.py`, find the GameHandler class and make sure it points to the right directory:

```python
class GameHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Make sure this path is correct
        super().__init__(*args, directory='./frontend', **kwargs)
```

If your HTML is directly in the root, use:
```python
super().__init__(*args, directory='.', **kwargs)
```

---

## Quick Fix: Deploy This Working Version

Here's a corrected `server.py` that definitely works on Railway:

```python
#!/usr/bin/env python3
import http.server
import socketserver
import json
import time
import random
import os
from urllib.parse import urlparse, parse_qs
from collections import defaultdict
import uuid

# ✅ USE RAILWAY'S PORT
PORT = int(os.environ.get('PORT', 8080))

# Game state
games = {}
player_sessions = {}

class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.players = []
        self.started = False
        self.deck = []
        self.flipped_cards = []
        self.current_player_turn = 0
        self.matched_cards = set()
        self.last_update = time.time()
        
    def add_player(self, session_id, player_name):
        if len(self.players) >= 5:
            return False
        player_id = len(self.players)
        self.players.append({
            'name': player_name,
            'score': 0,
            'id': player_id,
            'session_id': session_id
        })
        self.last_update = time.time()
        return True
    
    def remove_player(self, session_id):
        self.players = [p for p in self.players if p['session_id'] != session_id]
        self.last_update = time.time()
    
    def start_game(self):
        if len(self.players) < 2:
            return False
        self.started = True
        pig_items = ['🐷', '🐖', '🥓', '🌸', '🎀', '🐽', '💕', '⭐', '🎪', '🎯', '🎨', '🎭', '🍄', '🍎']
        self.deck = pig_items * 2
        random.shuffle(self.deck)
        self.current_player_turn = 0
        self.last_update = time.time()
        return True
    
    def flip_card(self, session_id, card_index):
        if not self.started:
            return {'error': 'Game not started'}
        
        player = next((p for p in self.players if p['session_id'] == session_id), None)
        if not player:
            return {'error': 'Player not found'}
        
        player_id = player['id']
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
        
        if len(self.flipped_cards) == 3:
            cards_values = [self.deck[i] for i in self.flipped_cards]
            if len(set(cards_values)) == 1:
                player['score'] += 1
                for idx in self.flipped_cards:
                    self.matched_cards.add(idx)
                result['match'] = True
                result['scorer'] = player_id
                result['new_score'] = player['score']
                
                if player['score'] >= 7:
                    result['winner'] = player_id
                    result['winner_name'] = player['name']
            else:
                result['match'] = False
                self.current_player_turn = (self.current_player_turn + 1) % len(self.players)
                result['next_turn'] = self.current_player_turn
            
            self.flipped_cards = []
        
        self.last_update = time.time()
        return result
    
    def to_dict(self):
        return {
            'game_id': self.game_id,
            'players': [{'id': p['id'], 'name': p['name'], 'score': p['score']} for p in self.players],
            'started': self.started,
            'current_turn': self.current_player_turn if self.started else None,
            'deck_size': len(self.deck),
            'matched_cards': list(self.matched_cards),
            'last_update': self.last_update
        }

class GameHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # ✅ SERVE FROM CURRENT DIRECTORY
        super().__init__(*args, directory='.', **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/api/poll':
            self.handle_poll()
        elif parsed_path.path == '/' or parsed_path.path == '':
            # Serve index.html
            self.path = '/frontend/index.html'
            super().do_GET()
        else:
            super().do_GET()
    
    def do_POST(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/api/action':
            self.handle_action()
        else:
            self.send_error(404)
    
    def handle_poll(self):
        parsed_path = urlparse(self.path)
        params = parse_qs(parsed_path.query)
        
        session_id = params.get('session', [None])[0]
        last_update = float(params.get('last_update', [0])[0])
        
        if session_id and session_id in player_sessions:
            game_id = player_sessions[session_id]
            if game_id in games:
                game = games[game_id]
                
                timeout = 25
                start = time.time()
                while time.time() - start < timeout:
                    if game.last_update > last_update:
                        break
                    time.sleep(0.2)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(game.to_dict()).encode())
                return
        
        self.send_response(204)
        self.end_headers()
    
    def handle_action(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        action = data.get('action')
        response = {}
        
        if action == 'create_game':
            player_name = data.get('name', 'Player')
            game_id = f"game_{str(uuid.uuid4())[:8]}"
            session_id = str(uuid.uuid4())
            
            game = Game(game_id)
            game.add_player(session_id, player_name)
            games[game_id] = game
            player_sessions[session_id] = game_id
            
            response = {
                'success': True,
                'game_id': game_id,
                'session_id': session_id,
                'player_id': 0
            }
        
        elif action == 'join_game':
            game_id = data.get('game_id')
            player_name = data.get('name', 'Player')
            session_id = str(uuid.uuid4())
            
            if game_id in games:
                game = games[game_id]
                if game.add_player(session_id, player_name):
                    player_sessions[session_id] = game_id
                    response = {
                        'success': True,
                        'session_id': session_id,
                        'player_id': len(game.players) - 1
                    }
                else:
                    response = {'success': False, 'error': 'Game full'}
            else:
                response = {'success': False, 'error': 'Game not found'}
        
        elif action == 'start_game':
            session_id = data.get('session_id')
            if session_id in player_sessions:
                game_id = player_sessions[session_id]
                game = games[game_id]
                if game.start_game():
                    response = {'success': True}
                else:
                    response = {'success': False, 'error': 'Need at least 2 players'}
            else:
                response = {'success': False, 'error': 'Session not found'}
        
        elif action == 'flip_card':
            session_id = data.get('session_id')
            card_index = data.get('card_index')
            
            if session_id in player_sessions:
                game_id = player_sessions[session_id]
                game = games[game_id]
                result = game.flip_card(session_id, card_index)
                response = {'success': 'error' not in result, **result}
            else:
                response = {'success': False, 'error': 'Session not found'}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

# ✅ BIND TO RAILWAY'S PORT
print(f"Starting Incha Porco server on http://0.0.0.0:{PORT}")

with socketserver.TCPServer(("0.0.0.0", PORT), GameHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
```

---

## How to Update Your Railway Deployment

### Option 1: Push to GitHub (Recommended)

```bash
# In your local folder
git add .
git commit -m "Fix PORT for Railway"
git push origin main
```

Railway will automatically redeploy!

### Option 2: Redeploy via Railway Dashboard

1. Go to your Railway project
2. Click on your deployment
3. Go to "Deployments" tab
4. Click "Redeploy"

### Option 3: Use Railway CLI

```bash
railway up
```

---

## Check Railway Logs

This is SUPER important for debugging:

1. Go to https://railway.app
2. Click on your project
3. Click on your service
4. Click "Deployments" tab
5. Click on the latest deployment
6. Click "View Logs"

**Look for:**
- ✅ "Starting Incha Porco server..."
- ✅ "Server running on port XXXXX"
- ❌ Any error messages

---

## Verify Your File Structure

Make sure you have this structure:

```
your-repo/
├── server.py          ✅ Updated with PORT fix
├── Procfile           ✅ Contains: web: python3 server.py
├── requirements.txt   ✅ Can be empty
├── runtime.txt        ✅ Contains: python-3.11.0
└── frontend/
    └── index.html     ✅ Your game interface
```

---

## Still Not Working? Try This:

1. **Delete and recreate the Railway deployment**
2. **Check the logs** for specific error messages
3. **Make sure all files are committed to GitHub**
4. **Verify Procfile has no extra characters**

---

## Test Locally First

Before deploying, always test:

```bash
export PORT=8080
python3 server.py
# Open http://localhost:8080
```

If it works locally, it should work on Railway!

---

## Contact Me

Tell me:
1. What you see in the Railway logs
2. What error message appears in browser (if any)
3. Your current file structure

I'll help you fix it! 🐷
