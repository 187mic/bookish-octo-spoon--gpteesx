"""
Simple test script for GPT configuration without requiring OpenAI package.
"""

import os
import sys
from gpt_config import load_gpt_config


def test_configuration():
    """Test the GPT configuration setup."""
    print("=" * 60)
    print("GPT Configuration Test")
    print("=" * 60)
    
    # Test 1: Missing API key
    print("\n[Test 1] Testing missing API key...")
    os.environ.pop('OPENAI_API_KEY', None)
    try:
        config = load_gpt_config()
        print("  ✗ FAIL: Should have raised ValueError")
        return False
    except ValueError as e:
        print(f"  ✓ PASS: {e}")
    
    # Test 2: Invalid API key format
    print("\n[Test 2] Testing invalid API key format...")
    os.environ['OPENAI_API_KEY'] = 'invalid-key'
    try:
        config = load_gpt_config()
        print("  ✗ FAIL: Should have raised ValueError")
        return False
    except ValueError as e:
        print(f"  ✓ PASS: {e}")
    
    # Test 3: Valid configuration
    print("\n[Test 3] Testing valid configuration...")
    os.environ['OPENAI_API_KEY'] = 'sk-test1234567890'
    os.environ['GPT_MODEL'] = 'gpt-4'
    os.environ['GPT_TEMPERATURE'] = '0.7'
    os.environ['GPT_MAX_TOKENS'] = '2000'
    
    try:
        config = load_gpt_config()
        print(f"  ✓ PASS: Configuration loaded")
        print(f"     {config}")
        
        # Verify client config
        client_config = config.get_client_config()
        assert 'api_key' in client_config
        print(f"  ✓ PASS: Client config has api_key")
        
        # Verify default params
        params = config.get_default_params()
        assert params['model'] == 'gpt-4'
        assert params['temperature'] == 0.7
        assert params['max_tokens'] == 2000
        print(f"  ✓ PASS: Default params are correct")
        
    except Exception as e:
        print(f"  ✗ FAIL: {e}")
        return False
    
    # Test 4: With organization ID
    print("\n[Test 4] Testing with organization ID...")
    os.environ['OPENAI_ORG_ID'] = 'org-123456'
    
    try:
        config = load_gpt_config()
        client_config = config.get_client_config()
        assert 'organization' in client_config
        assert client_config['organization'] == 'org-123456'
        print(f"  ✓ PASS: Organization ID configured correctly")
    except Exception as e:
        print(f"  ✗ FAIL: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = test_configuration()
    sys.exit(0 if success else 1)
