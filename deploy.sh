#!/usr/bin/env bash
set -e

APP_DIR="$HOME/grocery-list"
APP_FILE="Main.py"

cd "$APP_DIR"

echo "Pulling latest code..."
git fetch --all
git reset --hard origin/main

echo "Setting up virtual environment..."
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

echo "Stopping old app..."
pkill -f "$APP_FILE" || true

echo "Starting app..."
nohup python3 "$APP_FILE" > log.txt 2>&1 &

echo "Deployment complete."
