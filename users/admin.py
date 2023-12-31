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


admin.site.unregister(User)


@admin.register(User)
class UserMixinAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    readonly_fields = ('id',)


# admin.site.register(User, UserMixinAdmin)
admin.site.register(Profile)
