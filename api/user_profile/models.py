from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    reading_time_for_7_days = models.FloatField(default=0)
    reading_time_for_30_days = models.FloatField(default=0)

    def __str__(self):
        return (f"user={self.user.username}"
                f"reading_time_for_7_days={self.reading_time_for_7_days},"
                f"reading_time_for_30_days={self.reading_time_for_30_days}",)
