from rest_framework.viewsets import ModelViewSet

from api_books.models import Books
from api_books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    def get_queryset(self):
        return Books.objects.all()

    def get_serializer_class(self):
        return BooksSerializer
