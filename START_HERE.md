# 🎮 START HERE - Incha Porco Quick Setup

## 📥 Step 1: Download the Game

**You should have downloaded:** `incha-porco.zip`

**Extract it** to a folder on your computer.

---

## 🚀 Step 2: Choose How to Play

### Option A: Play Locally (Test with Friends on Same WiFi)
```bash
cd incha-porco
python3 server.py
```
Then open: http://localhost:8080

**Share with friends on same network:**
- Find your IP address (see below)
- Share: `http://YOUR-IP:8080`

**Finding your IP:**
- Mac/Linux: `ifconfig | grep inet`
- Windows: `ipconfig`
- Look for something like `192.168.1.X`

---

### Option B: Play Online (Friends Anywhere)

#### **Fastest: Use ngrok (5 minutes)**

1. Download ngrok: https://ngrok.com/download
2. Start your game:
   ```bash
   python3 server.py
   ```
3. In another terminal:
   ```bash
   ngrok http 8080
   ```
4. Share the ngrok URL with friends!

#### **Best: Deploy to Railway (10 minutes)**

📖 **See the detailed guide:** `RAILWAY_TUTORIAL.md`

**Quick version:**
1. Create GitHub account
2. Upload your `incha-porco` files to GitHub
3. Go to https://railway.app
4. Login with GitHub
5. Click "New Project" → "Deploy from GitHub"
6. Select your repository
7. Generate a domain
8. Share your permanent URL!

---

## 📁 Important Files

- **server.py** - The game server
- **frontend/index.html** - The game interface
- **Procfile** - For Railway deployment
- **requirements.txt** - For Railway deployment
- **RAILWAY_TUTORIAL.md** - Detailed Railway guide

---

## ❓ Need Help?

### "I can't run python3 server.py"

**Install Python:**
- Windows: https://www.python.org/downloads/
- Mac: `brew install python3`
- Linux: `sudo apt install python3`

### "I want to deploy to Railway but confused"

Read: `RAILWAY_TUTORIAL.md` - Step-by-step with screenshots explained!

### "Port 8080 already in use"

```bash
# Kill the process using the port
lsof -ti:8080 | xargs kill

# Or edit server.py and change:
PORT = 8081  # Use a different port
```

---

## 🎯 Quick Checklist

- [ ] Extracted the ZIP file
- [ ] Opened terminal/command prompt
- [ ] Navigated to incha-porco folder
- [ ] Ran `python3 server.py`
- [ ] Opened http://localhost:8080 in browser
- [ ] Created a game and tested it works
- [ ] Chose deployment method (ngrok or Railway)
- [ ] Shared URL with friends
- [ ] Started playing! 🐷

---

## 🌐 Deployment Comparison

| Method | Speed | Duration | Cost | Best For |
|--------|-------|----------|------|----------|
| **ngrok** | 5 min | Session only | Free | Quick test |
| **Railway** | 10 min | Permanent | Free tier | Long-term |
| **Render** | 15 min | Permanent | Free tier | Alternative |

**Recommendation:** Use ngrok for tonight, deploy to Railway for permanent access!

---

## 🎉 You're Ready!

1. Extract the ZIP
2. Run `python3 server.py`
3. Test locally
4. Deploy online
5. Share with friends
6. Play Incha Porco! 🐷

**Questions?** Check these files:
- `QUICKSTART.md` - Basic guide
- `RAILWAY_TUTORIAL.md` - Railway deployment
- `README.md` - Full documentation
- `DEPLOYMENT.md` - All deployment options

Have fun! 🎮
