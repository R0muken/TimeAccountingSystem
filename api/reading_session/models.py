from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from api.book.models import Book


class ReadingSession(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(
        null=True,
        blank=True)

    def save_reading_session(self):
        """
        Save the end time of a reading session and update the database.

        Returns:
            None
        """
        self.end_time = timezone.now()
        self.save()

    @classmethod
    def get_reading_time_for_n_days(cls, user_id, days: int):
        """
        Calculates reading time for n days

         Args:
            user_id (int).
            days (int):
         Returns:
            reading_session (ReadingSession): The ReadingSession instance to be updated.
        """
        current_time = timezone.now()
        time_n_days_ago = current_time - timezone.timedelta(days=days)

        reading_time = cls.objects.filter(
            user_id=user_id,
            start_time__gte=time_n_days_ago,
            end_time__lte=current_time
        ).aggregate(total_time=models.Sum(models.F('end_time') - models.F('start_time')))

        return reading_time

    def __str__(self):
        return (f"user={self.user.username}, "
                f"book={self.book.title}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})")
