from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Movie, MovieRating


@admin.register(Movie)
class PersonAdmin(ImportExportModelAdmin):
    pass


admin.site.register(MovieRating)
