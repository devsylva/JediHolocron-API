#!/bin/bash

# Detect the operating system
OS="$(uname)"

# Activate virtual environment based on the detected OS
if [[ "$OS" == "Darwin" ]]; then  # macOS
    source venv/bin/activate
elif [[ "$OS" == "Linux" ]]; then  # Linux
    source venv/bin/activate
elif [[ "$OS" == "MINGW"* ]]; then  # Windows (MinGW or Git Bash)
    source venv/Scripts/activate
else
    echo "Unsupported operating system: $OS"
    exit 1
fi

# install requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run update_film_data script 
python manage.py update_film_data

# Run development server
python manage.py runserver

# Deactivate virtual environment
deactivate
