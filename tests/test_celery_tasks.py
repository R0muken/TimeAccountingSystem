import pytest

from api.reading_session.tasks import calculate_user_reading_time
from api.user_profile.models import UserProfile


@pytest.mark.django_db(transaction=True)
def test_celery_calculate_reading_task(user_instance, sample_reading_session, celery_app, celery_worker):
    task_result = calculate_user_reading_time.delay(user_id=user_instance.id).get(timeout=10)

    user_profile = UserProfile.objects.get(user_id=user_instance.id)

    assert user_profile
    assert user_profile.reading_time_for_7_days == 86400
    assert task_result == 0

