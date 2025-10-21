# 🐷 Incha Porco - Multiplayer Pig Memory Game

Welcome to Incha Porco! A fun multiplayer memory card game with a pig theme.

## 🚀 MAKE IT PUBLIC NOW!

**Want your friends to play right now?** Start here:

### ⚡ [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) ← START HERE!
Quick checklist - choose a platform and deploy in 5 minutes!

### 🌟 [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md) ← RECOMMENDED!
Step-by-step Railway deployment (easiest, free, permanent)

### 📚 [DEPLOY_NOW.md](DEPLOY_NOW.md)
Complete guide with 6 deployment options (Railway, Render, ngrok, Vercel, Heroku, Replit)

---

## 📖 Documentation

### 🚀 [QUICKSTART.md](QUICKSTART.md)
Get the game running locally in 3 simple steps.

### 📘 [README.md](README.md)
Full documentation including features, rules, and technical details.

### 🌐 [DEPLOYMENT.md](DEPLOYMENT.md)
Original deployment guide with technical details.

### 📋 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
Complete overview of what was built and delivered.

---

## 🎮 Quick Start Locally

```bash
python3 server.py
```

Then open http://localhost:8080 in your browser!

---

## 🌍 Quick Start Publicly (RECOMMENDED)

### Option 1: Railway (5 minutes, FREE, permanent)
1. Go to https://railway.app
2. Sign up with GitHub
3. Upload your `incha-porco` folder
4. Generate domain
5. Share URL with friends!

### Option 2: ngrok (30 seconds, FREE, temporary)
```bash
python3 server.py          # Terminal 1
ngrok http 8080            # Terminal 2
# Share the ngrok URL!
```

**Full instructions:** See RAILWAY_DEPLOY.md or DEPLOY_NOW.md

---

## 📸 Screenshots

- `incha_porco_menu.png` - Main menu
- `incha_porco_waiting_p1.png` - Waiting room with players
- `incha_porco_game_p1.png` - Game board in action

---

## 🎯 Game Overview

- **Players**: 2-5 per game
- **Goal**: First to 7 points wins
- **How**: Match 3 identical cards to score 1 point
- **Theme**: Cute pig emojis 🐷
- **Sound**: Fart/oink effects on matches! 🎵

---

## 📁 Project Structure

```
incha-porco/
├── server.py                    # Run this to start the game
├── start.sh                     # Quick start script
├── frontend/
│   └── index.html              # Complete game interface  
├── test_game.py                # Automated tests
│
├── DEPLOYMENT_CHECKLIST.md     # ⚡ Deploy in 5 min checklist
├── RAILWAY_DEPLOY.md           # 🌟 Railway guide (recommended)
├── DEPLOY_NOW.md               # 📚 All deployment options
├── QUICKSTART.md               # Local setup
├── README.md                   # Full documentation
├── DEPLOYMENT.md               # Technical deployment info
├── PROJECT_SUMMARY.md          # What was built
│
├── railway.json                # Railway config
├── render.yaml                 # Render config
├── Procfile                    # Heroku config
├── runtime.txt                 # Python version
└── requirements.txt            # Dependencies (none!)
```

---

## ✨ Features

✅ Real-time multiplayer (2-5 players)
✅ Pig-themed cards with 14 different emojis
✅ Fun sound effects (fart & oink!)
✅ Turn-based gameplay
✅ Score tracking to 7 points
✅ Responsive design (mobile & desktop)
✅ No installation needed for players
✅ Easy game ID sharing

---

## 🔧 Requirements

- Python 3 (no external dependencies!)
- Modern web browser
- That's it!

---

## 🎪 Let's Play!

### Locally:
1. Run `python3 server.py`
2. Create a game
3. Share Game ID with friends on same network
4. Start playing!

### Publicly (so friends anywhere can join):
1. Deploy to Railway (see RAILWAY_DEPLOY.md)
2. Share your public URL once
3. Create games and share Game IDs
4. Play from anywhere! 🌍

---

**Have fun and may the best pig win!** 🐷🏆
