from rest_framework import serializers
from .models import ReadingSession


class ReadingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSession
        fields = ('id', 'user', 'book', 'start_time', 'end_time')