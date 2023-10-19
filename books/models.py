from django.db import models
from authors.models import Author  

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
