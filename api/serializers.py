from books.models import Book, Author, Language
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source="author.name", read_only=True)
    # publication_language = serializers.ReadOnlyField(
    #     source="publication_language.code", read_only=True
    # )
    author = serializers.CharField(max_length=64)
    publication_language = serializers.CharField(max_length=2)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        author = validated_data.pop("author")
        publication_language = validated_data.pop("publication_language")
        author_instance, created = Author.objects.get_or_create(name=author)
        publication_language_instance, created = Language.objects.get_or_create(
            code=publication_language
        )
        book_instance = Book.objects.create(
            **validated_data,
            author=author_instance,
            publication_language=publication_language_instance
        )
        return book_instance
