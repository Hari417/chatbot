#!/bin/bash

# Step 1: Create a virtual environment
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Install the required packages from requirements.txt
pip install -r requirements.txt

# Step 4: Pull the required model using Ollama
ollama pull deepseek-r1:14b

echo "Virtual environment setup complete. Model deepseek-r1:14b pulled. You can now run the Flask app."
