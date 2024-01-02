from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return (f"user={self.user.username}, "
                f"book={self.book.title}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})")
