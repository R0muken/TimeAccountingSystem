from rest_framework.pagination import PageNumberPagination


class BookPaginator(PageNumberPagination):
    page_size = 10
