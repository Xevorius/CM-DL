"""
collection/views.py: Contains the code for loading the HTML for each  of the base web app's webpages
"""

__author__ = "Tim Rietdijk"
__email__ = "tim.is@live.nl"
__status__ = "Development"

# third-party imports:
from django.shortcuts import render


def home(request):
    return render(request, 'collection/home.html', {'title': "Home"})
