from django.db import models
from isbn_field import ISBNField

# - Zamodeluj obiekty bazodanowe tak by zawierały pola:
#  tytuł, autor, data publikacji, numer ISBN, liczba stron,
#  link do okładki i język publikacji.


class Language(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code


class Author(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    date_published = models.PositiveIntegerField()
    ISBN_number = ISBNField(unique=True)
    pages = models.PositiveIntegerField()
    cover_url = models.URLField(max_length=512)
    publication_language = models.ForeignKey(Language, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
