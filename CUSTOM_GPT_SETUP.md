# Custom GPT Setup Guide for GitHub Integration

This guide will help you set up a Custom GPT that can interact with GitHub to create repositories, commit code, manage files, and more.

## Prerequisites

1. **ChatGPT Plus or Enterprise account** - Required to create Custom GPTs
2. **GitHub account** - For the repositories you want to manage
3. **GitHub Personal Access Token** - For authentication

## Step 1: Create GitHub Personal Access Token

1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
2. Click **"Generate new token (classic)"**
3. Give it a descriptive name (e.g., "ChatGPT GitHub Integration")
4. Select the following scopes:
   - ✅ **repo** (Full control of private repositories)
   - ✅ **user** (Read user profile data)
   - ✅ **workflow** (Update GitHub Action workflows)
5. Click **"Generate token"**
6. **Copy the token immediately** - you won't be able to see it again!
7. Save it securely (you'll use it in Step 3)

## Step 2: Create Your Custom GPT

1. Go to [ChatGPT](https://chat.openai.com/)
2. Click your profile picture → **"My GPTs"**
3. Click **"Create a GPT"**
4. Switch to the **"Configure"** tab

### Configure Basic Settings:

**Name:** GitHub Repository Manager

**Description:** An AI assistant that can create repositories, commit code, manage files, and perform GitHub operations through natural conversation.

**Instructions:** 
```
You are a GitHub Repository Manager assistant. You help users manage their GitHub repositories through natural conversation. You can:

- Create new repositories
- Add, update, and read files in repositories
- Create branches
- List commits
- Get repository information
- Manage code through commits

When the user asks you to perform GitHub operations:
1. Confirm what they want to do
2. Ask for any missing information (repository name, file path, commit message, etc.)
3. Execute the operation using the GitHub API
4. Provide clear feedback about what was done, including links to the created/modified resources

Always encode file contents in base64 when creating or updating files. For text files, encode the UTF-8 string to base64.

Be helpful and guide users through the process if they're unsure about what information you need.
```

**Conversation starters:**
- Create a new repository for me
- Add a README file to my repository
- Show me recent commits in my repo
- Create a new Python file in my project
- Help me set up a new project structure

## Step 3: Add GitHub API Action

1. Scroll down to the **"Actions"** section
2. Click **"Create new action"**
3. Configure the action:

**Authentication:**
- Type: **API Key**
- Auth Type: **Bearer**
- API Key: `[Paste your GitHub Personal Access Token here]`
- Custom Header Name: Leave as "Authorization"

**Schema:**
- Click **"Import from URL"** or **"Upload file"**
- If using file: Upload the `github-api-schema.yaml` file from this repository
- If using URL: You'll need to host the schema file somewhere accessible

**Privacy Policy:** (Optional but recommended)
- You can use GitHub's privacy policy: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement

4. Click **"Save"** or **"Update"**

## Step 4: Test Your Custom GPT

1. In the GPT Builder, go to the **"Preview"** pane
2. Try these test commands:

```
"Get my GitHub user information"
```

```
"Create a new repository called 'test-repo' with a description 'Testing ChatGPT integration'"
```

```
"Add a README.md file to my test-repo with content: # Test Repository\n\nThis is a test."
```

If everything works, you should see successful responses and be able to verify the changes on GitHub!

## Step 5: Publish Your GPT (Optional)

1. Click **"Save"** in the top right
2. Choose who can access it:
   - **Only me** - Private, just for you
   - **Anyone with a link** - Share with specific people
   - **Public** - Listed in GPT Store (requires verification)

## Using Your Custom GPT

Once set up, you can interact with your GPT naturally:

### Example Conversations:

**Create a new project:**
```
User: "Create a new repository called 'my-awesome-app' with a README and a basic Python project structure"
```

**Add code files:**
```
User: "Add a main.py file to my-awesome-app with a basic Flask application"
```

**Update existing files:**
```
User: "Update the README in my-awesome-app to include installation instructions"
```

**Check repository info:**
```
User: "Show me the recent commits in my-awesome-app"
```

## Troubleshooting

### "Authentication failed" errors
- Verify your GitHub token is correct and has the required scopes
- Check that the token hasn't expired
- Make sure you selected "Bearer" auth type in the action configuration

### "Not Found" errors
- Verify the repository name is correct
- Check that you have access to the repository
- Ensure you're using your GitHub username correctly

### File encoding issues
- The API requires base64 encoding for file contents
- The GPT should handle this automatically, but you can specify: "make sure to base64 encode the content"

### Rate limiting
- GitHub API has rate limits (5,000 requests/hour for authenticated requests)
- If you hit limits, wait an hour or use the token more sparingly

## Security Notes

⚠️ **Important Security Considerations:**

1. **Token Security**: Your GitHub token gives full access to your repositories. Treat it like a password.
2. **Token Permissions**: Only grant the minimum necessary scopes
3. **Token Rotation**: Regularly rotate your tokens (e.g., every 90 days)
4. **GPT Privacy**: If you share your GPT, others won't see your token, but they would use their own
5. **Audit Logs**: Check GitHub's security log regularly: https://github.com/settings/security-log

## Advanced Usage

### Creating Multi-File Projects

You can ask the GPT to create entire project structures:

```
"Create a new repository called 'flask-api' and set it up with:
- README.md explaining the project
- requirements.txt with Flask and other dependencies
- app.py with a basic Flask application
- .gitignore for Python projects
- Dockerfile for containerization"
```

### Working with Branches

```
"Create a new branch called 'feature-auth' in my flask-api repository"
```

### Updating Multiple Files

```
"In my flask-api repo, update both app.py and requirements.txt to add SQLAlchemy support"
```

## Additional Resources

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [OpenAI Custom GPTs Guide](https://help.openai.com/en/articles/8554397-creating-a-gpt)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review GitHub API status: https://www.githubstatus.com/
3. Check OpenAI status: https://status.openai.com/
4. Review your token permissions and expiration

---

**Note**: This Custom GPT interacts with the GitHub API through ChatGPT's action system. It does not run any local code - everything happens through API calls from ChatGPT to GitHub.
