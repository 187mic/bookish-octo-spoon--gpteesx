"""
Example GPT Client Usage

This script demonstrates how to use the GPT configuration 
with OpenAI's API for making chat completions.
"""

import sys
from gpt_config import load_gpt_config

try:
    from openai import OpenAI
except ImportError:
    print("OpenAI package not installed. Install with: pip install openai")
    sys.exit(1)


def create_gpt_client(config):
    """
    Create an OpenAI client with the provided configuration.
    
    Args:
        config: GPTConfig instance
        
    Returns:
        Configured OpenAI client
    """
    client_config = config.get_client_config()
    return OpenAI(**client_config)


def example_chat_completion(client, config, prompt: str):
    """
    Example function to make a chat completion request.
    
    Args:
        client: OpenAI client instance
        config: GPTConfig instance
        prompt: User prompt to send to GPT
        
    Returns:
        Response from GPT
    """
    default_params = config.get_default_params()
    
    try:
        response = client.chat.completions.create(
            model=default_params['model'],
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=default_params['temperature'],
            max_tokens=default_params['max_tokens']
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error making API call: {e}")
        return None


def main():
    """Main function demonstrating GPT configuration usage."""
    print("=" * 60)
    print("GPT Configuration Example")
    print("=" * 60)
    
    # Load configuration
    try:
        config = load_gpt_config()
        print(f"\n✓ Configuration loaded successfully!")
        print(f"  {config}")
    except ValueError as e:
        print(f"\n✗ Configuration error: {e}")
        print("\nPlease:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
    
    # Create client
    print("\n✓ Creating OpenAI client...")
    client = create_gpt_client(config)
    
    # Example usage
    print("\n" + "=" * 60)
    print("Testing GPT API Connection")
    print("=" * 60)
    
    test_prompt = "Say 'Hello! GPT configuration is working!' in a friendly way."
    print(f"\nPrompt: {test_prompt}")
    print("\nResponse:")
    print("-" * 60)
    
    response = example_chat_completion(client, config, test_prompt)
    
    if response:
        print(response)
        print("-" * 60)
        print("\n✓ GPT configuration is working correctly!")
    else:
        print("\n✗ Failed to get response from GPT")
        sys.exit(1)


if __name__ == "__main__":
    main()
