#!/bin/bash

# system detection
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows system
    echo "Windows system detected"
    python -m venv venv
    source venv/Scripts/activate
else
    # Mac/Linux system
    echo "Mac/Linux system detected"
    python3 -m venv venv
    source venv/bin/activate
fi

# install dependencies
pip install -r requirements.txt

echo "Virtual environment created and activated, dependencies installed"
echo "Use 'source venv/bin/activate' (Mac/Linux) or 'venv\Scripts\activate' (Windows) to activate the virtual environment"
