web: gunicorn sfswitch.wsgi --workers $WEB_CONCURRENCY --log-file -
worker: celery -A enable_disable.tasks worker -B
# worker: celery -A enable_disable.tasks worker -B --log-level debug
