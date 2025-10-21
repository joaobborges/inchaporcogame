# Delete the old Procfile
rm Procfile

# Create a new one with EXACTLY one line
echo "web: python3 server.py" > Procfile

# Verify it has only one line
cat Procfile

# Should show:
# web: python3 server.py

# Check line count (should be 1)
wc -l Procfile

# Commit and push
git add Procfile
git commit -m "Fix Procfile - remove extra lines"
git push
```

### **Method 2: Using Text Editor**

1. **Delete your Procfile completely**
2. **Create a NEW file named `Procfile`** (capital P, no extension)
3. **Type EXACTLY this (then hit Enter ZERO times):**
```
   web: python3 server.py