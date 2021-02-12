web: gunicorn sfswitch.wsgi --workers $WEB_CONCURRENCY --log-file - --log-level debug
worker: celery -A celeryapp worker -B --log-level debug
# worker: celery -A enable_disable.tasks worker -B --log-level debug
