from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from users.models import Profile


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
