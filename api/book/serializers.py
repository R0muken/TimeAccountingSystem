from rest_framework import serializers

from .models import Book


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "author", "publication_year", "short_description")


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ("updated",)
