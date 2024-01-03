from celery import shared_task
from django.contrib.auth.models import User
from config.celery import app
from api.reading_session.models import ReadingSession
from api.user_profile.models import UserProfile


@shared_task
def calculate_user_reading_time(user_id):
    """
    Calculate and update the reading time for a user over the last 7 and 30 days.

    Args:
        user_id (int): The ID of the user.
    Returns:
        int: A flag indicating the success of the operation.
    """

    reading_time_for_7_days = ReadingSession.get_reading_time_for_n_days(
        user_id=user_id,
        days=7)

    reading_time_for_30_days = ReadingSession.get_reading_time_for_n_days(
        user_id=user_id,
        days=30)

    user_profile, created = UserProfile.objects.get_or_create(user_id=user_id)

    if reading_time_for_7_days['total_time']:
        user_profile.reading_time_for_7_days = reading_time_for_7_days['total_time'].total_seconds()
        user_profile.reading_time_for_30_days = reading_time_for_30_days['total_time'].total_seconds()
    else:
        user_profile.reading_time_for_7_days = 0
        user_profile.reading_time_for_30_days = 0

    user_profile.save()
    return 0


@app.task
def calculate_reading_time_for_all_users():
    """
    Invokes 'calculate_user_reading_time' task for every User in database
    to calculate reading time.
    """
    user_ids = User.objects.values_list('id', flat=True)

    for user_id in user_ids:
        calculate_user_reading_time.delay(user_id)
