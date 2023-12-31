from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from books.models import BookAuthor, Book, BookRating


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(BookAuthor)
class BookAuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(BookRating)
class BookRatingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass