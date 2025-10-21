# 🚂 Deploy Incha Porco to Railway - Complete Tutorial

## What is Railway?

Railway is a cloud platform that makes it super easy to deploy apps. They have a **FREE tier** that's perfect for this game!

---

## Method 1: Deploy from GitHub (Recommended - 10 minutes)

### Step 1: Create a GitHub Account (if you don't have one)
1. Go to https://github.com
2. Click "Sign up"
3. Follow the registration steps

### Step 2: Upload Your Game to GitHub

1. **Create a new repository:**
   - Go to https://github.com/new
   - Repository name: `incha-porco`
   - Make it Public
   - Click "Create repository"

2. **Upload your files:**
   - Click "uploading an existing file"
   - Drag and drop these files from your computer:
     - `server.py`
     - `frontend/` folder (with index.html inside)
     - `Procfile` (we'll create this below)
     - `requirements.txt` (we'll create this below)
   - Click "Commit changes"

### Step 3: Create Required Files

Before uploading, create these two files:

**File 1: `Procfile`** (no extension)
```
web: python3 server.py
```

**File 2: `requirements.txt`**
```
# No external dependencies needed!
# Python 3's built-in libraries are sufficient
```

### Step 4: Deploy to Railway

1. **Sign up for Railway:**
   - Go to https://railway.app
   - Click "Login" then "Login with GitHub"
   - Authorize Railway to access your GitHub

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `incha-porco` repository
   - Click "Deploy Now"

3. **Configure Settings:**
   - Railway will automatically detect it's a Python app
   - It will use port 8080 by default
   - Click on your deployment
   - Go to "Settings" tab
   - Scroll to "Networking"
   - Click "Generate Domain"
   - Copy your public URL (e.g., `your-app.railway.app`)

4. **Done! 🎉**
   - Your game is now live!
   - Share the URL with your friends
   - They can access it from anywhere!

---

## Method 2: Deploy Using Railway CLI (Alternative - 5 minutes)

### Step 1: Install Railway CLI

**Mac/Linux:**
```bash
curl -fsSL https://railway.app/install.sh | sh
```

**Windows (PowerShell):**
```powershell
iwr https://railway.app/install.ps1 | iex
```

Or download from: https://docs.railway.app/guides/cli

### Step 2: Login

```bash
railway login
```

This will open your browser to authenticate.

### Step 3: Initialize and Deploy

```bash
cd incha-porco
railway init
railway up
```

### Step 4: Generate Public URL

```bash
railway domain
```

Railway will give you a public URL!

---

## Method 3: Deploy from Railway Dashboard (No Code Upload)

### Step 1: Prepare Files

Make sure your `incha-porco` folder has:
- `server.py`
- `frontend/index.html`
- `Procfile`
- `requirements.txt`

### Step 2: Create ZIP

Zip your entire `incha-porco` folder.

### Step 3: Deploy

1. Go to https://railway.app
2. Login with GitHub
3. Click "New Project"
4. Select "Empty Project"
5. Click "New" → "GitHub Repo" or use CLI to deploy

*Note: Railway works best with GitHub integration*

---

## Troubleshooting

### Issue: "Application failed to respond"

**Fix:** Make sure your `server.py` uses Railway's PORT environment variable:

Add this at the top of `server.py`:
```python
import os
PORT = int(os.environ.get('PORT', 8080))
```

And at the bottom, change:
```python
# FROM THIS:
with socketserver.TCPServer(("0.0.0.0", 8080), GameHandler) as httpd:

# TO THIS:
with socketserver.TCPServer(("0.0.0.0", PORT), GameHandler) as httpd:
```

### Issue: "Deployment keeps failing"

1. Check the logs in Railway dashboard
2. Make sure `Procfile` has exactly: `web: python3 server.py`
3. Verify all files uploaded correctly

### Issue: "Can't access the game"

1. Make sure you generated a domain in Railway settings
2. Check if deployment shows "Active" status
3. Try the URL in an incognito window

---

## Railway Free Tier Limits

✅ **What You Get FREE:**
- $5 credit per month (usually enough for small games)
- Up to 500 hours of runtime
- 1GB RAM
- 1GB Storage
- Perfect for hosting Incha Porco!

⚠️ **What Happens If You Run Out:**
- Your app will sleep
- You can upgrade to a paid plan ($5/month)
- Or wait for next month's credits

---

## Keeping Your Game Running 24/7

Railway apps stay running as long as you have credits. Tips:
- Start with free tier
- Monitor usage in dashboard
- Upgrade to Hobby plan ($5/month) if needed
- Your game uses minimal resources, so free tier should work!

---

## Alternative: Use Railway Template (FASTEST!)

I can help you create a Railway template button! But for now, manual deployment is most reliable.

---

## Summary

✅ **Easiest:** GitHub + Railway dashboard (10 min)  
⚡ **Fastest:** Railway CLI (5 min)  
🎯 **Best:** GitHub method (most reliable)

After deployment, you'll have a permanent URL like:
`https://incha-porco-production.railway.app`

Share this with your friends and start playing! 🐷🎮

---

## Need Help?

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Or use ngrok for instant testing: `ngrok http 8080`
