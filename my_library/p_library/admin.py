from django.contrib import admin
from p_library.models import Book, Author, Publisher

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass