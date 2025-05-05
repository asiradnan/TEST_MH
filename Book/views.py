from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @method_decorator(cache_page(60*60*24*365)) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Book.objects.all()
        author_name = self.request.query_params.get('author', None)
        
        if author_name is not None:
            # Filter on the name field of the related Author model
            queryset = queryset.filter(author__name__icontains=author_name)
            
        return queryset
