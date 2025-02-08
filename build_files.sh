#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run collectstatic to gather static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate
