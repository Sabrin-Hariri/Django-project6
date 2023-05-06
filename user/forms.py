from django import forms

from django.contrib.auth.forms import UserCreationForm ,User
from django.contrib.auth.models import User


class RegisterationForm(UserCreationForm):

    email=forms.EmailField(max_length=222)
    class Meta:
        model = User 
        fields= ['username' , 'email' , 'password1', 'password2']
