from django.db import models
from Author.models import Author

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_year = models.DateField(auto_now_add=True)
    is_archieved = models.BooleanField(default=False)   
