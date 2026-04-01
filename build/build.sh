#!/bin/bash

echo "Starting build process..."

# Exit on error
set -e

# Create virtual environment (optional)
echo "Setting up virtual environment..."
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations (if any)
# python manage.py migrate

echo "Build completed successfully!"