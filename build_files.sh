#!/bin/bash

# Exit if any command fails
set -e

# 1. Ensure Python 3.9 is installed
echo "Checking for Python 3.9..."
python3.9 --version || { echo "Python 3.9 not found! Please install it."; exit 1; }

# 2. Ensure pip is installed for Python 3.9
echo "Ensuring pip is installed for Python 3.9..."
python3.9 -m ensurepip --upgrade

# 3. Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
python3.9 -m pip install --upgrade pip  # Ensure pip is the latest version
python3.9 -m pip install -r requirements.txt

# 4. Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

# 5. Apply migrations to the database
echo "Applying database migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# 6. (Optional) If you're using a production-ready web server like Gunicorn, you can add:
# echo "Starting Gunicorn..."
# gunicorn myproject.wsgi:application --bind 0.0.0.0:8000

# 7. (Optional) Restart your server or services if needed
# echo "Restarting server..."
# sudo systemctl restart myproject

echo "Build and deployment complete!"
