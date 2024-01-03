import time
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.reading_session.models import ReadingSession
from api.book.models import Book


class ReadingSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def get_book(self, pk: int):
        """
        Retrieves a book from the database based by pk.

        Args:
            pk (int): The primary key of the book.
        Returns:
            The Book instance or None.
        """
        try:
            book = Book.objects.get(id=pk)
            return book
        except Book.DoesNotExist:
            return None

    def post(self, request, pk: int):
        """
        Handles request to end or start a reading session for a specific book.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): Primary key of the book to retrieve.
        Returns:
            Response: success message or a failure message if the book does not exist.
        """
        book = self.get_book(pk)
        if not book:
            return Response({"status": "fail", "message": "Book not found"}, 404)

        user = request.user

        active_session_with_current_book = ReadingSession.objects.filter(user=user, book=book, end_time=None).first()
        if active_session_with_current_book:
            active_session_with_current_book.save_reading_session()
            return Response({"status": "success", 'message': "Reading session ended successfully"})

        active_session_with_another_book = ReadingSession.objects.filter(user=user, end_time=None).first()
        if active_session_with_another_book:
            active_session_with_another_book.save_reading_session()

        ReadingSession.objects.create(user=user, book=book)
        return Response({"status": "success", "message": "Reading session started successfully"})


class ReadingSessionUserStatisticView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Handles the request to retrieve user's reading statistics.

        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: User's reading statistics.
        """
        user = request.user
        reading_sessions = ReadingSession.objects.filter(user=user, end_time__isnull=False)

        reading_time = sum([(session.end_time - session.start_time).total_seconds() for session in reading_sessions])

        result = {"books_read": len({session.book_id for session in reading_sessions}),
                  "reading_sessions": len(reading_sessions),
                  "reading_time": time.strftime("%H:%M:%S", time.gmtime(reading_time))}
        return Response(result)


class ReadingSessionBooksStatisticView(APIView):

    def get(self, request):
        """
        Handles the request to retrieve user's reading statistics per book.

        Args:
            request (HttpRequest): The HTTP request object.
        Returns:
            Response: User's reading statistics per book.
        """
        user = request.user
        reading_sessions = ReadingSession.objects.filter(user=user, end_time__isnull=False)

        books_reading_statistic = {}
        for session in reading_sessions:
            book_id = session.book.id
            reading_time = (session.end_time - session.start_time).total_seconds()
            books_reading_statistic[session.book.title] = books_reading_statistic.get(book_id, 0) + reading_time

        result = [
            {
                "title": book_title,
                "reading_time": time.strftime("%H:%M:%S", time.gmtime(reading_time))
            }
            for book_title, reading_time in books_reading_statistic.items()
        ]
        return Response(result)
