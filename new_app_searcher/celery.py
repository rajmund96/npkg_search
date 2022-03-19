import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_app_searcher.settings')

app = Celery('new_app_searcher')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
