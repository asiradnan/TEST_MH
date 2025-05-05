from rest_framework import serializers
from .models import Book
from Author.serializers import AuthorSerializer 

class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_details']
