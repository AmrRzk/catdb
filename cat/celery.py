from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cat.settings')

app = Celery('cat')

app.conf.timezone = "Asia/Singapore"

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'update-breed-everyday':  {
        'task': 'sitecat.tasks.update_breed',
        'schedule': crontab(hour=17, minute=2),
    }
}

app.autodiscover_tasks()
