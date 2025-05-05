from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name 
