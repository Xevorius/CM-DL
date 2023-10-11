from time import timezone

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from books.models import Book, BookAuthor
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now login.')
            return redirect('login')
    else:
        context = {
            'form': UserRegisterForm(),
            'title': 'Register'
        }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form,
        'books': BookAuthor.objects.filter(author=request.user)
    }

    return render(request, 'users/profile.html', context)


def user_detail(request, pk):
    context = {'user': User.objects.get(pk=int(pk)), 'books': BookAuthor.objects.filter(author_id=pk), 'profile': Profile.objects.get(user=pk)}
    return render(request, 'user_page.html', context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['books'] = Book.objects.all().filter(pk=BookAuthor.objects.filter(author=self.kwargs['pk']))
    #     return context
