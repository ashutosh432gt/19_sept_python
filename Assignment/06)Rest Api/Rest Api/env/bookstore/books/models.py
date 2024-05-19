from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title
