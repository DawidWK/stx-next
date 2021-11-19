from django import forms
from .models import Book


class QueryBooksForm(forms.ModelForm):
    from_date = forms.DateField()
    to_date = forms.DateField()

    class Meta:
        model = Book
        fields = ["title", "author", "publication_language"]


class BookForm(forms.ModelForm):
    author = forms.CharField(max_length=64)
    publication_language = forms.CharField(max_length=2)

    class Meta:
        model = Book
        fields = ["title", "date_published", "ISBN_number", "pages", "cover_url"]
