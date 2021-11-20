from rest_framework import viewsets
from .serializers import BookSerializer
from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        books = Book.objects.all()
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        publication_language = self.request.query_params.get("publication_language")
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")
        if title is not None:
            books = books.filter(title__contains=title)
        if author is not None:
            books = books.filter(author=author)
        if publication_language is not None:
            books = books.filter(publication_language=publication_language)
        if from_date is not None:
            books = books.filter(date_published__gte=from_date)
        if to_date is not None:
            books = books.filter(date_published__lte=to_date)

        return books
