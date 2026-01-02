# GPT Configuration with Auth Token

A simple and secure way to configure OpenAI GPT API with authentication token management.

## Features

- ✅ Secure authentication token management using environment variables
- ✅ Configurable GPT model parameters (model, temperature, max_tokens)
- ✅ Easy-to-use configuration module
- ✅ Example usage script demonstrating API integration
- ✅ Input validation and error handling

## Setup

### Quick Setup (Recommended)

Run the setup script to automatically install dependencies and configure your environment:

```bash
bash setup.sh
```

Then edit `.env` to add your OpenAI API key.

### Manual Setup

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2. Configure Authentication

Copy the example environment file and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

#### 3. (Optional) Customize GPT Settings

You can customize the GPT model settings in your `.env` file:

```env
GPT_MODEL=gpt-4
GPT_TEMPERATURE=0.7
GPT_MAX_TOKENS=2000
OPENAI_ORG_ID=your-org-id  # Optional
```

## Usage

### Basic Configuration

```python
from gpt_config import load_gpt_config

# Load configuration from .env file
config = load_gpt_config()

# Get client configuration
client_config = config.get_client_config()
print(client_config)  # {'api_key': 'sk-...'}

# Get default parameters
params = config.get_default_params()
print(params)  # {'model': 'gpt-4', 'temperature': 0.7, 'max_tokens': 2000}
```

### Using with OpenAI Client

```python
from openai import OpenAI
from gpt_config import load_gpt_config

# Load configuration
config = load_gpt_config()

# Create OpenAI client
client = OpenAI(**config.get_client_config())

# Make API call with default parameters
params = config.get_default_params()
response = client.chat.completions.create(
    model=params['model'],
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=params['temperature'],
    max_tokens=params['max_tokens']
)

print(response.choices[0].message.content)
```

### Run Example Script

To test your configuration:

```bash
python example_usage.py
```

This will:
1. Load your configuration
2. Create an OpenAI client
3. Make a test API call
4. Display the response

## Configuration Options

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | - | ✅ Yes |
| `GPT_MODEL` | GPT model to use | `gpt-4` | No |
| `GPT_TEMPERATURE` | Response randomness (0-2) | `0.7` | No |
| `GPT_MAX_TOKENS` | Maximum response length | `2000` | No |
| `OPENAI_ORG_ID` | Organization ID | - | No |

## Security

- **Never commit** your `.env` file with actual API keys
- The `.gitignore` file is configured to exclude `.env` files
- API keys are validated to ensure they start with `sk-`
- The configuration class masks API keys in string representations

## Error Handling

The configuration module includes validation:

```python
from gpt_config import load_gpt_config

try:
    config = load_gpt_config()
except ValueError as e:
    print(f"Configuration error: {e}")
    # Handle missing or invalid API key
```

## Requirements

- Python 3.7+
- openai >= 1.0.0
- python-dotenv >= 1.0.0

## Getting an API Key

1. Go to [OpenAI's website](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

## Important: This is for OpenAI API, Not ChatGPT App

⚠️ **Common Confusion**: This configuration is for using the **OpenAI API** in Python scripts, NOT for:
- ChatGPT web interface (chat.openai.com)
- Custom GPTs
- ChatGPT mobile app
- GitHub Copilot

### What You Need

This repository requires an **OpenAI API Key** (starts with `sk-`), which is different from:
- ❌ GitHub personal access tokens
- ❌ ChatGPT Plus subscription
- ❌ GitHub OAuth tokens

### If You Want to Use This Code

1. **Get OpenAI API Access**: Visit [platform.openai.com](https://platform.openai.com/api-keys)
2. **Create API Key**: Generate a new API key (starts with `sk-`)
3. **Add to .env**: Put your key in the `.env` file as `OPENAI_API_KEY=sk-...`
4. **Run Python Scripts**: Use this code in Python scripts on your machine

### If You Want to Use ChatGPT App/Custom GPTs

This repository is **not designed** for ChatGPT app integration. For Custom GPTs:
- Use ChatGPT's action builder interface
- Configure API endpoints and authentication there
- No need for this repository

## Troubleshooting

### "GPT agent keeps getting blocked"

If you're trying to use this with ChatGPT or GitHub:
- This code is for **direct OpenAI API** usage in Python
- ChatGPT app and Custom GPTs use a different authentication method
- GitHub tokens are not used for OpenAI API access

### "Invalid API key format"

Make sure your API key:
- Starts with `sk-`
- Is from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Is not a GitHub token or OAuth key

### "Configuration error"

Check that:
1. `.env` file exists in the project root
2. `OPENAI_API_KEY` is set in `.env`
3. API key is valid and has not been revoked
4. Python dependencies are installed: `pip install -r requirements.txt`

## License

See LICENSE file for details.