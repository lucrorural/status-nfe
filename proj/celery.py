import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'status_portal_nfe': {
        'task': 'task_status_portal_nfe',
        'schedule': 10 * 60,  # 10 minutes
    }
}
