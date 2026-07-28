import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro.settings")

app = Celery("pro")

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)

app.autodiscover_tasks()

# import os

# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings')

# app = Celery('pro')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.

# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()

# # app.conf.worker_enable_remote_control = False

# import time

# @app.task
# def add(x,y):
#     time.sleep(10)
#     return x+y

# # @app.task(bind=True, ignore_result=True)
# # def debug_task(self):
# #     print(f'Request: {self.request!r}')import os

