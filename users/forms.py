from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
