# 🌐 Deploying Incha Porco for Public Access

Since this environment doesn't support persistent public servers, here are several easy ways to deploy your game so friends can play from anywhere:

## Option 1: Using ngrok (Fastest - 5 minutes)

ngrok creates a secure tunnel to your local server, giving you a public URL instantly.

### Steps:
1. Download ngrok from https://ngrok.com/download
2. Start your game server:
   ```bash
   cd incha-porco
   python3 server.py
   ```
3. In a new terminal, run:
   ```bash
   ngrok http 8080
   ```
4. Share the generated URL (looks like: `https://abc123.ngrok.io`)
5. Your friends can now access the game!

**Pros**: Instant, no setup
**Cons**: Free tier has usage limits, URL changes each time

---

## Option 2: Deploy to Railway (Free tier available)

Railway offers free hosting for small projects.

### Steps:
1. Create account at https://railway.app
2. Create new project → Deploy from GitHub repo
3. Or use Railway CLI:
   ```bash
   npm i -g @railway/cli
   railway login
   railway init
   railway up
   ```
4. Railway will automatically detect Python and deploy
5. Get your public URL from the Railway dashboard

**Pros**: Persistent URL, stays running 24/7
**Cons**: Requires GitHub account or CLI setup

---

## Option 3: Deploy to Heroku

### Steps:
1. Install Heroku CLI: https://devcli.heroku.com/install
2. Create a `Procfile` in the incha-porco directory:
   ```
   web: python3 server.py
   ```
3. Create a `runtime.txt`:
   ```
   python-3.11.0
   ```
4. Deploy:
   ```bash
   cd incha-porco
   heroku login
   heroku create incha-porco-game
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   heroku open
   ```

**Pros**: Reliable, well-documented
**Cons**: Free tier has limited hours/month

---

## Option 4: Deploy to Render (Free tier)

### Steps:
1. Create account at https://render.com
2. New → Web Service
3. Connect your GitHub repo or deploy from Dashboard
4. Configure:
   - Build Command: (leave empty)
   - Start Command: `python3 server.py`
   - Environment: Python 3
5. Deploy!

**Pros**: Easy setup, stays running
**Cons**: May sleep after inactivity on free tier

---

## Option 5: DigitalOcean App Platform

### Steps:
1. Create DigitalOcean account
2. Create new App
3. Upload your code or connect GitHub
4. Configure as Python app
5. Deploy

**Pros**: Professional hosting, scalable
**Cons**: Costs $5/month (but very reliable)

---

## Quick Test Locally

Before deploying, test locally:

```bash
cd incha-porco
python3 server.py
```

Then visit `http://localhost:8080` in your browser!

To test with friends on the same network:
1. Find your local IP: `ifconfig` (Mac/Linux) or `ipconfig` (Windows)
2. Share: `http://YOUR_LOCAL_IP:8080`
3. Make sure your firewall allows port 8080

---

## Recommended: ngrok for Quick Testing, Railway/Render for Permanent Hosting

For a quick game session tonight: **Use ngrok**
For ongoing access: **Deploy to Railway or Render**

Both are free and take just minutes to set up!

---

## Port Configuration

If you need to change the port (default is 8080), edit `server.py`:

```python
PORT = 8080  # Change this to your desired port
```

Then update your deployment configuration accordingly.

---

## Environment Variables (for production)

For production deployments, you might want to:

1. Set the host in environment variables
2. Add SSL/HTTPS support (most platforms handle this automatically)
3. Add rate limiting for API endpoints
4. Store game state in a database (for persistence across restarts)

Current setup uses in-memory storage, so games reset when server restarts.

---

## Need Help?

- ngrok docs: https://ngrok.com/docs
- Railway docs: https://docs.railway.app
- Render docs: https://render.com/docs
- Heroku docs: https://devcli.heroku.com

Happy gaming! 🐷🎮
