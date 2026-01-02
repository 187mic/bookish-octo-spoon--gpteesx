"""
GPT Configuration Module

This module handles OpenAI GPT configuration and authentication.
It loads settings from environment variables and provides a configured client.
"""

import os
from typing import Optional
from dotenv import load_dotenv


class GPTConfig:
    """Configuration class for OpenAI GPT API."""
    
    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize GPT configuration.
        
        Args:
            env_file: Path to .env file. If None, uses default .env
        """
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()
        
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.org_id = os.getenv('OPENAI_ORG_ID')
        self.model = os.getenv('GPT_MODEL', 'gpt-4')
        self.temperature = float(os.getenv('GPT_TEMPERATURE', '0.7'))
        self.max_tokens = int(os.getenv('GPT_MAX_TOKENS', '2000'))
        
        self._validate()
    
    def _validate(self):
        """Validate required configuration."""
        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY is required. "
                "Please set it in your .env file or environment variables."
            )
        
        if not self.api_key.startswith('sk-'):
            raise ValueError(
                "Invalid OPENAI_API_KEY format. "
                "API key should start with 'sk-'"
            )
    
    def get_client_config(self) -> dict:
        """
        Get configuration dictionary for OpenAI client.
        
        Returns:
            Dictionary with client configuration
        """
        config = {
            'api_key': self.api_key,
        }
        
        if self.org_id:
            config['organization'] = self.org_id
        
        return config
    
    def get_default_params(self) -> dict:
        """
        Get default parameters for GPT API calls.
        
        Returns:
            Dictionary with default parameters
        """
        return {
            'model': self.model,
            'temperature': self.temperature,
            'max_tokens': self.max_tokens,
        }
    
    def __repr__(self) -> str:
        """String representation (hides API key)."""
        return (
            f"GPTConfig(model={self.model}, "
            f"temperature={self.temperature}, "
            f"max_tokens={self.max_tokens}, "
            f"api_key={'*' * 8 if self.api_key else None})"
        )


def load_gpt_config(env_file: Optional[str] = None) -> GPTConfig:
    """
    Convenience function to load GPT configuration.
    
    Args:
        env_file: Path to .env file. If None, uses default .env
        
    Returns:
        Configured GPTConfig instance
    """
    return GPTConfig(env_file=env_file)
