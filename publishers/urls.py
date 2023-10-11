from django.urls import path
from publishers.views import PublisherListView, PublisherDetailView

urlpatterns = [
    path("<pk>/", PublisherDetailView.as_view(), name="publisher-detail"),
    path("", PublisherListView.as_view(), name="publisher-list"),
]