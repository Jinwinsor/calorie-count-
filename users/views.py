from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Congratulations!{username} You are now registered.')
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
