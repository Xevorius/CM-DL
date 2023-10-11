from django.urls import path

from users import views

urlpatterns = [
    path("<pk>/", views.user_detail, name="user-detail"),
]