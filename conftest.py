from datetime import datetime, timedelta, timezone

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from api.book.models import Book
from api.reading_session.models import ReadingSession


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_instance():
    user = get_user_model().objects.create_user(
        username='testuser',
        password='testpassword',
        email='testuser@example.com',
    )
    return user


@pytest.fixture
def sample_reading_session(sample_book, user_instance):
    current_time = datetime.now(timezone.utc)

    reading_session = ReadingSession(
        user=user_instance,
        book=sample_book,
        end_time=current_time-timedelta(days=1))
    reading_session.save()

    reading_session.start_time = current_time-timedelta(days=2)
    reading_session.save()


@pytest.fixture
def sample_book():
    return Book.objects.create(
        title='Test Book',
        author='Test Author',
        short_description='Test Content',
        full_description="Full Test Content",
        last_read_date='2023-12-30')
