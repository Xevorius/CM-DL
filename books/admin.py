from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from books.models import BookAuthor


# @admin.register(BookAuthor)
# class PersonAdmin(ImportExportModelAdmin):
#     pass
#
#
# admin.site.register(BookAuthor)
