from rest_framework import serializers

from api_books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        exclude = []
