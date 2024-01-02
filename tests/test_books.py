import pytest


@pytest.mark.django_db
def test_book_list_view(api_client, sample_book):
    url = '/api/book/'
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == sample_book.title


@pytest.mark.django_db
def test_book_detail_view(api_client, sample_book):
    url = f'/api/book/{sample_book.id}/'
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data['title'] == sample_book.title


@pytest.mark.django_db
def test_book_detail_view_not_found(api_client):
    url = f'/api/book/{999}/'
    response = api_client.get(url)

    assert response.status_code == 404
    assert response.data == {"status": "fail", "message": "Book not found"}
