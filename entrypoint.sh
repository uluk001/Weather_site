# Collect static files
python3 manage.py collectstatic --noinput

# Apply database migrations
python3 manage.py migrate

# Start server
python3 manage.py runserver 0.0.0.0:8000