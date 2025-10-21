# ⚡ Deploy to Railway in 5 Minutes

## 🎯 Fastest Way to Get Your Friends Playing!

Railway offers the easiest deployment with a generous free tier. No credit card needed!

---

## Step 1: Create Railway Account (1 minute)

1. Go to **https://railway.app**
2. Click **"Start a New Project"**
3. Sign up with GitHub (or email)
4. Verify your email

---

## Step 2: Deploy Your Game (2 minutes)

### Option A: Deploy from Computer

1. Click **"New Project"**
2. Select **"Empty Project"**
3. Click **"Deploy from GitHub"** or **"Deploy from Local"**
4. If from local:
   - Click on the service
   - Go to **"Settings"**
   - Click **"Connect Repo"** or upload your `incha-porco` folder

### Option B: Use Railway CLI (Advanced)

```bash
# Install Railway CLI
npm i -g @railway/cli

# Navigate to your game
cd incha-porco

# Login and deploy
railway login
railway init
railway up
```

---

## Step 3: Configure (Auto-detected!) (30 seconds)

Railway automatically detects:
- ✅ Python environment
- ✅ Start command: `python3 server.py`
- ✅ Port configuration

You don't need to do anything! The included `railway.json` file handles it all.

---

## Step 4: Get Your Public URL (1 minute)

1. In your Railway dashboard, click on your deployment
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** section
4. Click **"Generate Domain"**
5. You'll get a URL like: `https://incha-porco-production.up.railway.app`

**✨ That's it! Your game is now live!**

---

## Step 5: Share with Friends! 🎉

Send your friends:

```
🐷 Let's play Incha Porco! 🐷

Game: https://[YOUR-URL].railway.app

How to play:
1. Click the link
2. Enter your name
3. I'll share the Game ID when I create the room
4. First to 7 points wins!

See you in the game! 🎮
```

---

## 🎮 How to Play Together

### As Host:
1. Open your Railway URL
2. Enter your name
3. Click "Create New Game"
4. **Share the Game ID** with friends (e.g., `game_abc123`)
5. Wait for friends to join
6. Click "Start Game"

### As Friend:
1. Open the Railway URL
2. Enter your name
3. Enter the Game ID from your friend
4. Click "Join Game"
5. Wait for host to start
6. Play!

---

## 📊 Railway Free Tier Details

- **Hours**: 500 hours/month (plenty for gaming!)
- **Always On**: Your game stays running 24/7
- **No Sleep**: Instant access (unlike Render)
- **No Credit Card**: Completely free to start
- **Execution Time**: Pay only if you exceed 500 hrs

**Perfect for hosting your pig game! 🐷**

---

## 🔧 Monitoring Your Deployment

### View Logs
1. Go to your project in Railway
2. Click on your service
3. Click "Logs" tab
4. See real-time server activity

### Check Status
- Green indicator = Running perfectly
- Yellow = Deploying
- Red = Error (check logs)

---

## 🚀 Pro Tips

1. **Bookmark your Railway URL** - You'll use it often!
2. **Test first** - Create a test game before inviting friends
3. **Share the Game ID via text/Discord** - Not the full URL
4. **Multiple games** - Players can join different Game IDs on the same URL
5. **Keep Railway tab open** - Monitor active games in real-time

---

## ⚠️ Troubleshooting

**"Application failed to start"**
- Wait 2-3 minutes for initial deployment
- Check logs for errors
- Redeploy if needed

**"Can't access the URL"**
- Make sure domain is generated
- Try hard refresh (Ctrl+F5)
- Check if deployment is active

**"Game not loading"**
- Clear browser cache
- Try incognito mode
- Check Railway service status

---

## 🎯 What Happens Next?

After deployment:
- ✅ Your game is live 24/7
- ✅ Friends can join anytime
- ✅ Multiple game sessions can run simultaneously
- ✅ No maintenance required!

---

## 📱 Mobile Access

Your Railway URL works perfectly on:
- 📱 iPhones
- 📱 Android phones
- 💻 Tablets
- 💻 Computers

Just share the link and play from anywhere!

---

## 🎉 You're Live!

**Total time: ~5 minutes**
**Cost: $0.00**
**Difficulty: Easy**

Your friends can now play Incha Porco from anywhere in the world!

**Start deploying now:** https://railway.app

---

## Need Another Option?

If Railway doesn't work for you, check out **DEPLOY_NOW.md** for 5 more hosting options including:
- Render (also free)
- ngrok (instant, temporary)
- Vercel (super fast)
- Replit (browser-based)
- Heroku (classic)

But Railway is definitely the easiest! 🚂

---

**Have fun playing with your friends!** 🐷🎮
