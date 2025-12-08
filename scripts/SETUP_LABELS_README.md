# GitHub Labels Automation Script

## Overview

This script automates the creation and assignment of GitHub labels across all your repositories based on a predefined mapping. It's part of the **Repository Organization Phase 3** initiative.

## Quick Start

### 1. Install Dependencies

```bash
pip install PyGithub python-dotenv
```

### 2. Create GitHub Personal Access Token (PAT)

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Give it a name: `Repository Labels Automation`
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org data if applicable)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again)

### 3. Set Environment Variable

```bash
# Linux/Mac
export GITHUB_TOKEN='your_token_here'

# Windows (PowerShell)
$env:GITHUB_TOKEN='your_token_here'

# Or add to .env file (if using python-dotenv)
echo "GITHUB_TOKEN=your_token_here" > .env
```

### 4. Run the Script

```bash
python scripts/setup_labels.py
```

## What the Script Does

### 1. Creates 16 Labels

**Status Labels** (5):
- `active` - Actively developed
- `paused` - Development on hold
- `maintenance-only` - Bug fixes only
- `archived` - Legacy projects
- `deprecated` - No longer used

**Feature Labels** (5):
- `ai-powered` - Uses AI/LLM
- `app-core` - Main business application
- `integration` - Third-party integrations
- `experimental` - POCs & tests
- `documentation` - Docs & specifications

**Type Labels** (5):
- `typescript` - TypeScript/JavaScript
- `python` - Python
- `fullstack` - Frontend + Backend
- `frontend` - UI focused
- `open-source` - Public contributions

**Audience Labels** (2):
- `commercial` - Business/Wii Group
- `personal-project` - Personal use

### 2. Assigns Labels to Repositories

Each repository gets assigned 3-5 relevant labels based on its category and purpose. Labels are added as GitHub Topics for easy discoverability.

## Output Example

```
============================================================
GitHub Repository Labels Automation
============================================================

✓ Connected as: Flavio459

Processing: Alma-Ego
  Setting up labels in Alma-Ego...
    ✓ Created label: active
    ✓ Created label: ai-powered
    ...
  Assigning 5 labels to repository...
    ✓ Added 5 labels as topics

...

============================================================
SUMMARY
============================================================
Repositories processed: 26
Labels created: 112
Labels assigned: 128
Errors: 0
============================================================

✅ All repositories labeled successfully!
```

## Troubleshooting

### "GITHUB_TOKEN environment variable not set!"

Make sure you've set the environment variable. Check:

```bash
echo $GITHUB_TOKEN  # Linux/Mac
echo $env:GITHUB_TOKEN  # Windows PowerShell
```

### "Bad credentials" or "401 Unauthorized"

- Token may have expired or been revoked
- Token scope may be insufficient (needs `repo` scope)
- Generate a new token and try again

### "Repository not found"

- Repository name may not match exactly
- Check the `REPO_LABELS_MAP` in `setup_labels.py`
- Ensure you have access to the repository

### "Rate limit exceeded"

GitHub has API rate limits (5000 requests/hour for authenticated users). If this happens:

1. Wait an hour, or
2. Modify the script to add delays between requests

## Customization

### Adding a New Repository

Edit `setup_labels.py` and add to `REPO_LABELS_MAP`:

```python
REPO_LABELS_MAP = {
    'my-new-repo': ['app-core', 'typescript', 'active', 'commercial'],
    ...
}
```

### Changing Label Colors

Edit `LABEL_CONFIG` in `setup_labels.py`:

```python
LABEL_CONFIG = {
    'active': {
        'color': '28a745',  # Change this hex color
        'description': 'Actively developed'
    },
    ...
}
```

### Modifying Label Assignments

Edit the `REPO_LABELS_MAP` dictionary to change which labels are assigned to each repo.

## Important Notes

⚠️ **Security:**
- Never commit your GitHub token to version control
- Use environment variables or `.env` files (add `.env` to `.gitignore`)
- Tokens should be treated like passwords

✅ **Idempotent:**
- The script is safe to run multiple times
- It won't fail if labels already exist
- It will skip existing labels gracefully

📊 **Statistics:**
- Total repos: 26
- Total labels to create: 16
- Total assignments: ~120 label associations
- Estimated time: 2-3 minutes

## Next Steps

After running the script:

1. ✅ Visit your GitHub profile to verify labels are assigned
2. ✅ Use labels to filter/organize repositories
3. ✅ Update `REPOSITORY_MAP.md` with label updates
4. ✅ Consider Phase 4: Repository renaming and archival

## Related Files

- `REPOSITORY_MAP.md` - Complete mapping of all 26 repositories
- `setup_labels.py` - The automation script
- `SETUP_LABELS_README.md` - This file

## Support

If you encounter issues:

1. Check the error message in the output
2. Review the troubleshooting section
3. Verify your GitHub token is valid
4. Check `REPOSITORY_MAP.md` for repository names

---

**Created:** December 8, 2025
**Updated:** December 8, 2025
**Status:** Ready for production use ✅
