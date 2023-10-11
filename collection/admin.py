from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from books.models import Book, BookRating, BookAuthor


@admin.register(Book)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(BookAuthor)
class PersonAdmin(ImportExportModelAdmin):
    pass


admin.site.register(BookRating)


