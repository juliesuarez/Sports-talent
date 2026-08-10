#!/bin/sh

# If the DB_HOST is set, wait for the database to be ready
if [ "$DB_HOST" = "db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Execute the CMD from Dockerfile or docker-compose
exec "$@"