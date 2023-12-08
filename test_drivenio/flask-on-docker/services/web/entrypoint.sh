#!/bin/sh
# Make sure Postgres is up and healthy before creating
# the database table and running the Flask development server

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # The nc -z command checks whether a connection can be established without transferring data.
    # nc is netcat
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db

exec "$@"

