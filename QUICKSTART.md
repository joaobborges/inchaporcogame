# 🚀 Quick Start Guide - Incha Porco

## Get Playing in 3 Steps!

### Step 1: Start the Server
```bash
cd incha-porco
python3 server.py
```

You should see:
```
Starting Incha Porco server on http://0.0.0.0:8080
Access the game at: http://0.0.0.0:8080/
```

### Step 2: Open in Browser
- Open your web browser
- Go to: `http://localhost:8080`

### Step 3: Play!
1. **Host**: Enter your name → Click "Create New Game"
2. **Share** the Game ID with friends
3. **Friends**: Enter name + Game ID → Click "Join Game"  
4. **Start**: Host clicks "Start Game" when everyone's ready
5. **Play**: Take turns flipping 3 cards at a time, match to score!

---

## Playing Online with Friends

### Easiest Method: ngrok
```bash
# Terminal 1: Start game
python3 server.py

# Terminal 2: Create public tunnel
ngrok http 8080
```

Share the ngrok URL with friends (e.g., `https://abc123.ngrok.io`)

---

## Game Rules at a Glance

- 🎯 **Goal**: First to 7 points wins
- 🃏 **How to score**: Match 3 identical cards = 1 point
- 👥 **Players**: 2-5 players per game
- 🔄 **Turns**: Automatic turn rotation
- 🎵 **Sound**: Fart or oink on each match!

---

## Troubleshooting

**Port already in use?**
```bash
# Kill existing server
lsof -ti:8080 | xargs kill

# Or change port in server.py
PORT = 8081  # Use a different port
```

**Can't connect?**
- Check firewall settings
- Make sure server is running
- Try `http://127.0.0.1:8080` instead

**Game won't start?**
- Need at least 2 players
- Make sure all players joined before starting

---

## Screenshots

Check out these screenshots to see the game in action:
- `incha_porco_menu.png` - Main menu
- `incha_porco_waiting_p1.png` - Waiting room
- `incha_porco_game_p1.png` - Game board

---

## Files Overview

- `server.py` - Game server (run this!)
- `frontend/index.html` - Complete game interface
- `test_game.py` - Automated tests
- `README.md` - Full documentation
- `DEPLOYMENT.md` - Public hosting guide

---

## Next Steps

✅ You've got a working game!
💡 Want to deploy it? See `DEPLOYMENT.md`
🧪 Want to test it? Run `python3 test_game.py`
🎨 Want to customize? Edit `frontend/index.html`

---

Have fun playing Incha Porco! 🐷🎮

Questions? Check the README.md for more details.
