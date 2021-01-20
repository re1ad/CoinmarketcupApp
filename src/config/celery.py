import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'write_coins_30s': {
        'task': 'coins.tasks.write_coins',
        'schedule': 10.0
    }
}
app.autodiscover_tasks()

# celery -A config beat -l INFO
# celery -A config worker -l INFO
