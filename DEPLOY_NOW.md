# 🚀 Deploy Incha Porco - Step-by-Step Guide

Your game is ready to deploy! Choose one of these options to make it publicly accessible.

---

## 🎯 RECOMMENDED: Railway (Easiest + Free)

### Why Railway?
- ✅ Completely FREE tier (500 hours/month)
- ✅ No credit card required
- ✅ Takes 5 minutes
- ✅ Permanent public URL
- ✅ Auto-restarts if crashes

### Steps:

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub (or email)

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - OR click "Empty Project" and drag/drop your `incha-porco` folder

3. **Configure (if needed)**
   - Railway auto-detects Python
   - It will use the included `railway.json` config
   - Start command: `python3 server.py`

4. **Get Your Public URL**
   - Click on your deployment
   - Go to "Settings" → "Networking"
   - Click "Generate Domain"
   - You'll get: `https://incha-porco-production.up.railway.app`

5. **Share with Friends!**
   - Send them the URL
   - They can start playing immediately!

**Total Time: ~5 minutes**

---

## 🌟 ALTERNATIVE 1: Render (Also Free)

### Steps:

1. **Create Render Account**
   - Go to https://render.com
   - Sign up (free)

2. **New Web Service**
   - Click "New +" → "Web Service"
   - Connect GitHub repo OR upload folder

3. **Configure**
   - Name: `incha-porco`
   - Environment: `Python 3`
   - Build Command: (leave empty)
   - Start Command: `python3 server.py`
   - Instance Type: Free

4. **Deploy**
   - Click "Create Web Service"
   - Wait ~2 minutes for deployment
   - Get your URL: `https://incha-porco.onrender.com`

**Note**: Free tier may sleep after 15 min of inactivity. First load takes ~30 seconds.

---

## 🔥 ALTERNATIVE 2: Vercel (Super Fast)

### Steps:

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   cd incha-porco
   vercel
   ```

3. **Follow Prompts**
   - Login to Vercel
   - Confirm project name
   - Get instant URL!

**Time: 2 minutes**

---

## 💻 ALTERNATIVE 3: Heroku (Classic)

### Steps:

1. **Install Heroku CLI**
   - Download from https://devcli.heroku.com/install

2. **Deploy**
   ```bash
   cd incha-porco
   heroku login
   heroku create incha-porco-game
   git init
   git add .
   git commit -m "Deploy Incha Porco"
   git push heroku main
   heroku open
   ```

**Note**: Free tier has limited hours per month.

---

## ⚡ ALTERNATIVE 4: ngrok (Temporary but Instant)

### Best for: Quick testing or one-time game sessions

### Steps:

1. **Download ngrok**
   - Go to https://ngrok.com/download
   - Or: `brew install ngrok` (Mac) / `choco install ngrok` (Windows)

2. **Start Game Server**
   ```bash
   cd incha-porco
   python3 server.py
   ```

3. **Create Tunnel** (in new terminal)
   ```bash
   ngrok http 8080
   ```

4. **Share URL**
   - Look for the "Forwarding" URL: `https://abc123.ngrok.io`
   - Send this to friends!

**Pros**: Instant (30 seconds)
**Cons**: URL changes each time, free tier has limits

---

## 🎮 ALTERNATIVE 5: Replit (No Installation)

### Steps:

1. **Go to Replit.com**
   - Create free account

2. **Create New Repl**
   - Click "+ Create"
   - Choose "Import from GitHub" or "Upload files"
   - Upload your `incha-porco` folder

3. **Configure**
   - Replit auto-detects Python
   - Click "Run" button
   - Replit provides public URL automatically

4. **Share**
   - Copy the URL from browser
   - Send to friends!

**Time: 3 minutes**

---

## 📱 ALTERNATIVE 6: Glitch (Fun & Easy)

### Steps:

1. **Go to Glitch.com**
   - Sign up (free)

2. **New Project**
   - Click "New Project" → "Import from GitHub"
   - Or create empty project and upload files

3. **Auto-Deploy**
   - Glitch automatically runs Python apps
   - Get instant URL: `https://incha-porco.glitch.me`

---

## 🎯 Which One Should I Choose?

| Platform | Setup Time | Reliability | Free Tier | Permanent URL |
|----------|-----------|-------------|-----------|---------------|
| **Railway** | 5 min | ⭐⭐⭐⭐⭐ | 500hrs/mo | ✅ Yes |
| **Render** | 5 min | ⭐⭐⭐⭐ | Unlimited | ✅ Yes |
| **ngrok** | 30 sec | ⭐⭐⭐ | Limited | ❌ Temp |
| **Vercel** | 2 min | ⭐⭐⭐⭐⭐ | Good | ✅ Yes |
| **Heroku** | 10 min | ⭐⭐⭐⭐ | Limited | ✅ Yes |
| **Replit** | 3 min | ⭐⭐⭐ | Good | ✅ Yes |

### 🏆 **Best Choice: Railway**
- Easiest setup
- Most generous free tier
- Most reliable
- Perfect for your use case

---

## 🛠️ After Deployment

### Test Your Deployment

1. Open the public URL in your browser
2. Create a game
3. Note the Game ID
4. Open in incognito/another browser
5. Join using the Game ID
6. Start playing!

### Share with Friends

Send them:
```
🐷 Let's play Incha Porco! 🐷

Join the game at: [YOUR_PUBLIC_URL]

Game ID: [YOUR_GAME_ID]

Rules:
- Match 3 cards to score
- First to 7 points wins!
- Have fun! 🎮
```

---

## 🔧 Troubleshooting

**Port Issues?**
- Most platforms automatically assign ports
- Our server uses PORT environment variable (Heroku, Railway)
- Default is 8080 for local testing

**Server Not Starting?**
- Check logs in platform dashboard
- Ensure `server.py` is in root directory
- Verify Python 3 is selected

**Can't Connect?**
- Wait 1-2 minutes after deployment
- Try hard refresh (Ctrl+F5)
- Check platform status page

---

## 💡 Pro Tips

1. **Use Railway or Render for permanent hosting**
2. **Use ngrok for quick testing tonight**
3. **Keep your Game IDs short and memorable**
4. **Test with friends before big game night**
5. **Bookmark your deployment URL**

---

## 📞 Need Help?

- Railway Support: https://railway.app/help
- Render Docs: https://render.com/docs
- ngrok Docs: https://ngrok.com/docs
- This project folder includes all config files needed!

---

## 🎉 You're Ready!

All deployment configs are included:
- `railway.json` ✅
- `render.yaml` ✅
- `Procfile` ✅
- `runtime.txt` ✅
- `requirements.txt` ✅

Just follow the steps above for your chosen platform!

**Let the pig games begin!** 🐷🎮
