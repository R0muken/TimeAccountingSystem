from django.urls import path

from .views import ReadingSessionView, ReadingSessionUserStatisticView, ReadingSessionBooksStatisticView

urlpatterns = [
    path("reading-sessions/<int:pk>/", ReadingSessionView.as_view(),
         name="start_reading_session"),
    path("reading-sessions/user-statistic/", ReadingSessionUserStatisticView.as_view(),
         name="user_reading_statistic"),
    path("reading-sessions/books-statistic/", ReadingSessionBooksStatisticView.as_view(),
         name="user_reading_statistic_per_book"),
]