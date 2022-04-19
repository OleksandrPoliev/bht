from django.db import models

from .Validators import ISBN_validator


class BooksModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=200)
    ISBN = models.IntegerField(validators=[ISBN_validator])
    num_pages = models.IntegerField()
    book_img = models.URLField()
    book_language = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Create your models here.
