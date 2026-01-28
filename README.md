# ChatGPT GitHub Integration

Use ChatGPT to interact with GitHub - create repositories, commit code, manage files, and more through natural conversation.

## What This Does

This repository provides the configuration needed to create a **Custom GPT** that can:

- ✅ Create new GitHub repositories
- ✅ Add, update, and read files in repositories  
- ✅ Create branches and manage repository structure
- ✅ Commit code and track changes
- ✅ List commits and repository information
- ✅ Manage projects through natural conversation

## Quick Start

### 1. Get Your GitHub Token

Go to [GitHub Settings > Tokens](https://github.com/settings/tokens) and create a new token with these scopes:
- `repo` (Full control of private repositories)
- `user` (Read user profile data)
- `workflow` (Update GitHub Action workflows)

**Save your token securely - you'll need it in the next step!**

### 2. Create Your Custom GPT

1. Go to [ChatGPT](https://chat.openai.com/)
2. Click your profile → **"My GPTs"** → **"Create a GPT"**
3. Follow the detailed setup guide in **[CUSTOM_GPT_SETUP.md](./CUSTOM_GPT_SETUP.md)**

### 3. Import the GitHub API Schema

In your Custom GPT's Actions section:
- Upload the `github-api-schema.yaml` file from this repository
- Configure Bearer token authentication with your GitHub token

### 4. Start Using It!

Talk to your GPT naturally:

```
"Create a new repository called 'my-project' with a README"
```

```
"Add a Python file called main.py with a basic Flask application"
```

```
"Show me the recent commits in my repository"
```

## What's Included

📄 **`github-api-schema.yaml`** - OpenAPI schema for GitHub API integration  
📘 **`CUSTOM_GPT_SETUP.md`** - Detailed step-by-step setup guide  
📝 **`.env.example`** - Template for storing your GitHub token locally (optional)  
🔒 **`.gitignore`** - Protects your tokens from being committed

## Requirements

- **ChatGPT Plus or Enterprise** - Required to create Custom GPTs
- **GitHub Account** - For the repositories you'll manage
- **GitHub Personal Access Token** - For authentication

## Example Use Cases

### Create a New Project

```
User: "Create a new repository called 'flask-api' and set it up as a basic Flask REST API 
with a README, requirements.txt, and main application file"
```

### Add Code to Existing Repository

```
User: "In my flask-api repository, add a new endpoint for user authentication"
```

### Manage Files

```
User: "Update the README in my flask-api repo to include installation instructions and API documentation"
```

### Check Repository Status

```
User: "Show me the last 5 commits in my flask-api repository"
```

## How It Works

```
You (ChatGPT) ←→ Custom GPT ←→ GitHub API ←→ Your Repositories
```

1. You chat with your Custom GPT naturally
2. The GPT interprets your request and calls the GitHub API
3. GitHub performs the operation (create repo, commit code, etc.)
4. The GPT confirms what was done and provides links

**No local code execution** - everything happens through ChatGPT's action system and GitHub's API.

## Security

🔐 **Your GitHub token is secure:**
- Stored only in your Custom GPT's action configuration
- Not visible to others even if you share your GPT
- Can be rotated anytime from GitHub settings

⚠️ **Best Practices:**
- Only grant minimum necessary token scopes
- Rotate tokens regularly (every 90 days)
- Review GitHub's security log periodically
- Never commit your actual token to the repository

## Detailed Setup

For complete step-by-step instructions, see **[CUSTOM_GPT_SETUP.md](./CUSTOM_GPT_SETUP.md)**

The guide includes:
- Detailed token creation steps
- Custom GPT configuration instructions
- Example prompts and conversations
- Troubleshooting common issues
- Advanced usage patterns

## Troubleshooting

**Authentication Errors:**
- Verify your GitHub token is valid and hasn't expired
- Check that you selected the correct scopes when creating the token
- Ensure Bearer auth is configured correctly in the action

**File Operation Errors:**
- The API requires base64 encoding for file contents (the GPT handles this automatically)
- Verify repository names and paths are correct
- Check that you have write access to the repository

**Rate Limiting:**
- GitHub API allows 5,000 requests/hour for authenticated requests
- If you hit limits, wait an hour or reduce API calls

## What Changed?

This repository previously contained Python code for OpenAI API configuration. It has been updated to provide Custom GPT configuration for GitHub integration instead.

If you're looking for Python OpenAI API configuration, you'll need a different solution.

## Contributing

Feel free to:
- Report issues with the API schema
- Suggest additional GitHub API endpoints to include
- Share example use cases and prompts
- Improve the documentation

## Resources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [OpenAI Custom GPTs Guide](https://help.openai.com/en/articles/8554397-creating-a-gpt)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

## License

See [LICENSE](./LICENSE) file for details.
