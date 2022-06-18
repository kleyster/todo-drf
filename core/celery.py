from __future__ import absolute_import
from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings',namespace="CELERY")
app.autodiscover_tasks()