import os
import environ
import datetime as dt

from celery import Celery

SETTINGS_DEBUG = "config.settings.local"
SETTINGS_PRODUCTION = "config.settings.production"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_DEBUG)
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'say_hello': {
        'task': 'testproject_1.users.tasks.say_hello',
        'schedule': dt.timedelta(seconds=300),
    },
}