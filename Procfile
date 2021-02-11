web: gunicorn sfswitch.wsgi --workers $WEB_CONCURRENCY --log-file=-
worker: celery -A enable_disable.tasks worker -B --loglevel=DEBUG
