from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from books.models import BookRating
from movies.models import MovieRating
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-warning bg-dark text-white'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border-warning bg-dark text-white'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-warning bg-dark text-white'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border-warning bg-dark text-white'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.Field(widget=forms.ClearableFileInput(attrs={'class': 'btn btn-outline-warning bg-dark text-white'}))

    class Meta:
        model = Profile
        fields = ['image']


class GiveMovieRatingForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'border-warning bg-dark text-white'}))

    class Meta:
        model = MovieRating
        fields = ['rating']


class GiveBookRatingForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'border-warning bg-dark text-white'}))

    class Meta:
        model = BookRating
        fields = ['rating']