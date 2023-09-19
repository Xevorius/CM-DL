"""
collection/url.py: contains the routing for the base web app.
"""

__author__ = "Tim Rietdijk"
__email__ = "tim.is@live.nl"
__status__ = "Development"

# third-party imports:
from django.urls import path

# local imports:
from . import views

urlpatterns = [
    path('', views.home, name='collection-home'),
]
