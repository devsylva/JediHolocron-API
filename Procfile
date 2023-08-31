web: gunicorn jediholocron.wsgi --log-file -
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py update_film_data