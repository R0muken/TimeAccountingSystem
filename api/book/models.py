from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=45,
        blank=True)
    author = models.CharField(
        max_length=45,
        blank=True)
    publication_year = models.PositiveIntegerField(default=0)
    short_description = models.TextField(
        max_length=180,
        blank=True)
    full_description = models.TextField(blank=True)
    last_read_date = models.DateField(blank=True)
    updated = models.DateTimeField(
        auto_now=True,
        blank=True)

    def __str__(self):
        return (f"title={self.title},"
                f"author={self.author}",
                f"publication_year={self.publication_year},"
                f"short_description={self.short_description},"
                f"last_read_date={self.last_read_date},"
                f"updated={self.updated}")
