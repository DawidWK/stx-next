from django.test import TestCase
from .models import Author, Book, Language
from django.urls import reverse


class BasicTest(TestCase):
    def setUp(self):
        self.author = Author()
        self.author.name = "J. R. R. Tolkien"
        self.author.save()

        self.language = Language()
        self.code = "en"
        self.language.save()

        self.book = Book()
        self.book.title = "Hobbit"
        self.book.author = self.author
        self.book.date_published = "1937"
        self.book.ISBN_number = "9780044403371"
        self.book.pages = "310"
        self.book.cover_url = "https://en.wikipedia.org/wiki/The_Hobbit#/media/File:TheHobbit_FirstEdition.jpg"
        self.book.publication_language = self.language
        self.book.save()

    def test_fields(self):
        record = Book.objects.get(pk=1)
        self.assertEqual(record, self.book)

    def test_language_code(self):
        language = Language()
        language.code = "PL"
        language.save()
        self.assertEqual(language.code, "pl")

    def test_books_context(self):
        response = self.client.get(reverse("books"))

        self.assertEqual(response.context["books"][0], self.book)
