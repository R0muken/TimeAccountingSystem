from datetime import timedelta
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "reading_statistic_cronjob": {
        "task": "api.reading_session.tasks.calculate_reading_time_for_all_users",
        "schedule": timedelta(days=1),
    }
}

