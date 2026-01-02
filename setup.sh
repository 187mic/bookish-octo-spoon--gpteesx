#!/bin/bash

# Setup script for GPT Configuration
# This script helps users set up their environment quickly

set -e

echo "=========================================="
echo "GPT Configuration Setup"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is not installed. Please install Python 3.7 or later."
    exit 1
fi
echo "✓ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "✗ pip is not installed. Please install pip."
    exit 1
fi
echo "✓ pip found"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt --quiet
echo "✓ Dependencies installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit the .env file and add your OpenAI API key"
    echo ""
    echo "   1. Open .env in your text editor"
    echo "   2. Replace 'your_openai_api_key_here' with your actual API key"
    echo "   3. Get your API key from: https://platform.openai.com/api-keys"
    echo ""
else
    echo ""
    echo "✓ .env file already exists"
fi

# Run tests
echo ""
echo "Running configuration tests..."
if python3 test_config.py > /dev/null 2>&1; then
    echo "✓ Configuration tests passed!"
else
    echo "✗ Tests failed - this is expected if you haven't set your API key yet"
    echo ""
    echo "Next steps:"
    echo "  1. Edit .env and add your OpenAI API key"
    echo "  2. Run: python3 test_config.py"
    echo "  3. Run: python3 example_usage.py"
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
