from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Book, Author, Language
from .forms import BookForm, QueryBooksForm
import requests

# Create your views here.


def books(request):
    form = QueryBooksForm(use_required_attribute=False)
    books = Book.objects.all()

    if request.method == "GET" and request.GET:
        title = request.GET.get("title")
        author = request.GET.get("author")
        publication_language = request.GET.get("publication_language")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")

        if title != "":
            books = books.filter(title__contains=title)
        if author != "":
            books = books.filter(author=author)
        if publication_language != "":
            books = books.filter(publication_language=publication_language)
        if from_date != "":
            books = books.filter(date_published__gte=from_date)
        if to_date != "":
            books = books.filter(date_published__lte=to_date)
    context = {"books": books, "form": form}
    return render(request, "index.html", context)


def import_books(request):
    errors = []

    if request.POST:
        query = request.POST["query"]
        r = requests.get("https://www.googleapis.com/books/v1/volumes", {"q": query})

        for item in r.json()["items"]:
            title = item["volumeInfo"].get("title")
            author = item["volumeInfo"].get("authors")
            date_published = item["volumeInfo"].get("publishedDate").split("-")
            ISBN_number = item["volumeInfo"].get("industryIdentifiers")
            pages = item["volumeInfo"].get("pageCount")
            cover_url = item["volumeInfo"].get("imageLinks")
            publication_language = item["volumeInfo"].get("language")

            if author:
                author = author[0]
            if ISBN_number:
                ISBN_number = ISBN_number[0]["identifier"]
            if cover_url:
                cover_url = cover_url["thumbnail"]

            date_published = date_published[0]
            model_author = Author.objects.get_or_create(name=author)
            model_language = Language.objects.get_or_create(code=publication_language)

            try:
                model_book = Book.objects.create(
                    title=title,
                    author=model_author[0],
                    date_published=date_published,
                    ISBN_number=ISBN_number,
                    pages=pages,
                    cover_url=cover_url,
                    publication_language=model_language[0],
                )
                model_book.save()
            except Exception as e:
                errors.append(
                    {
                        "title": title,
                        "author": author,
                        "date_published": date_published,
                        "ISBN_number": ISBN_number,
                        "pages": pages,
                        "cover_url": cover_url,
                        "publication_language": publication_language,
                        "error": e,
                    }
                )
    context = {"errors": errors}
    return render(request, "import_books.html", context)


class BookFormView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "add_book.html"
    success_url = "/"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        tmp_form = form.save(commit=False)
        tmp_form.author = Author.objects.get_or_create(
            name=form.cleaned_data["author"]
        )[0]
        tmp_form.publication_language = Language.objects.get_or_create(
            code=form.cleaned_data["publication_language"]
        )[0]
        self.object = tmp_form.save()
        return super().form_valid(form)
