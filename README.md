# 🐷 Incha Porco - Multiplayer Pig Memory Game 🐷

A fun multiplayer memory card game where 2-5 players compete to find matching sets of three cards featuring adorable pig-themed illustrations!

## Game Rules

- **Players**: 2-5 players per game
- **Goal**: Be the first to reach 7 points
- **How to Score**: Match 3 identical cards to earn 1 point
- **Sound Effects**: Each successful match triggers a fun fart or oink sound! 🎵

## How to Play

### Creating a Game
1. Enter your name
2. Click "Create New Game"
3. Share the Game ID with your friends

### Joining a Game
1. Enter your name
2. Enter the Game ID shared by your friend
3. Click "Join Game"
4. Wait for the host to start the game

### Playing
- Wait for your turn (indicated by the highlighted player card)
- Click on 3 cards to flip them
- If all 3 cards match, you score 1 point and get another turn!
- If they don't match, the cards flip back and it's the next player's turn
- First player to reach 7 points wins! 🏆

## Running the Server

### Start the server:
```bash
cd /home/claude/incha-porco
python3 server.py
```

The game will be available at: `http://localhost:8080`

### For public access:
You'll need to:
1. Deploy to a cloud service (Heroku, Railway, DigitalOcean, etc.)
2. Or use a tunneling service like ngrok:
   ```bash
   ngrok http 8080
   ```
   This will give you a public URL to share with friends!

## Features

- **Real-time Multiplayer**: Multiple players can join and play simultaneously
- **Pig Theme**: Cute pig emojis and themed illustrations (🐷, 🐖, 🥓, 🌸, 🎀, 🐽, etc.)
- **Sound Effects**: Fun fart and oink sounds when you score
- **Responsive Design**: Works on desktop and mobile devices
- **Simple Interface**: Easy to learn and play
- **Score Tracking**: Live score updates for all players
- **Turn Indicators**: Clear visual indication of whose turn it is

## Technical Details

- **Backend**: Python HTTP server with long-polling
- **Frontend**: Pure HTML, CSS, and JavaScript
- **No external dependencies**: Works with Python 3's built-in libraries
- **Browser-based**: No installation required for players

## Testing

A test suite is included to verify multiplayer functionality:
```bash
python /mnt/skills/user/webapp-testing/scripts/with_server.py \
  --server "python3 server.py" --port 8080 \
  -- python3 test_game.py
```

## Development

- `server.py`: Main game server with API endpoints
- `frontend/index.html`: Complete game interface
- `test_game.py`: Playwright-based automated tests

## Game ID Format

Game IDs are automatically generated in the format: `game_XXXXXXXX`
Where X is a random hexadecimal character. This makes it easy to share!

Enjoy playing Incha Porco with your friends! 🐷🎮
