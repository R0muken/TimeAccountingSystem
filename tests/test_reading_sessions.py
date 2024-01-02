import pytest

from api.reading_session.models import ReadingSession


@pytest.mark.django_db
def test_reading_session_view_start_session(api_client, sample_book, user_instance):
    url = f'/api/reading-sessions/{sample_book.id}/'
    api_client.force_authenticate(user=user_instance)

    response = api_client.post(url)

    assert response.status_code == 200
    assert response.data == {"status": "success", 'message': 'Reading session started successfully'}
    assert ReadingSession.objects.filter(user=user_instance, book=sample_book, end_time=None).exists()


@pytest.mark.django_db
def test_reading_session_view_end_session(api_client, sample_book, user_instance):
    reading_session = ReadingSession.objects.create(user=user_instance, book=sample_book)
    url = f'/api/reading-sessions/{sample_book.id}/'
    api_client.force_authenticate(user=user_instance)

    response = api_client.post(url)

    assert response.status_code == 200
    assert response.data == {"status": "success", 'message': 'Reading session ended successfully'}
    assert ReadingSession.objects.get(id=reading_session.id).end_time is not None


@pytest.mark.django_db
def test_reading_session_view_book_not_found(api_client, user_instance):
    url = f'/api/reading-sessions/{999}/'
    api_client.force_authenticate(user=user_instance)

    response = api_client.post(url)

    assert response.status_code == 404
    assert response.data == {"status": "fail", "message": "Book not found"}


@pytest.mark.django_db
def test_reading_session_user_statistic_view(api_client, user_instance):
    url = f'/api/reading-sessions/user-statistic/'
    api_client.force_authenticate(user=user_instance)

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data.get('books_read') == 0
    assert response.data.get('reading_sessions') == 0
    assert response.data.get('reading_time') == '00:00:00'


@pytest.mark.django_db
def test_reading_session_books_statistic_view(api_client, user_instance):
    url = f'/api/reading-sessions/books-statistic/'
    api_client.force_authenticate(user=user_instance)

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data == []
