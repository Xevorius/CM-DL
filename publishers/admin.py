from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from publishers.models import Publisher, BookPublisher


@admin.register(Publisher)
class PublisherAdmin(ImportExportModelAdmin):
    readonly_fields = ('id',)


@admin.register(BookPublisher)
class BookPublisherAdmin(ImportExportModelAdmin):
    pass

