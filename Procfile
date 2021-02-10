web: gunicorn sfswitch.wsgi --workers $WEB_CONCURRENCY
web: celery -A enable_disable.tasks worker -B --loglevel=info
# worker: celery -A enable_disable.tasks worker -B --loglevel=info