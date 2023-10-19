from rest_framework import serializers
from authors.serializers import AuthorSerializer  
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
