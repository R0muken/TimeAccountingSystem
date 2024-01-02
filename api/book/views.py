from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .paginators import BookPaginator
from .serializers import BookListSerializer, BookDetailSerializer


class BookListView(ListAPIView):
    """
        Handles the request to retrieve all books
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookPaginator


class BookDetailView(APIView):
    def get(self, request, pk):
        """
            Handles the request to retrieve a book by its pk

            Args:
                request (HttpRequest): The HTTP request object.
            Returns:
                Response: A book
        """
        try:
            book = Book.objects.get(id=pk)
            serializer = BookDetailSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"status": "fail", "message": "Book not found"}, 404)
