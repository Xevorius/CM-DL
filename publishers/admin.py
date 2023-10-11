from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from publishers.models import Publisher, BookPublisher


@admin.register(Publisher)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(BookPublisher)
class PersonAdmin(ImportExportModelAdmin):
    pass

