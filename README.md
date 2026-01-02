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

## License

See LICENSE file for details.