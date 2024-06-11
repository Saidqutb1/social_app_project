from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUSer


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUSer
        fields = ('username', 'email', 'profile_picture')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUSer
        fields = ('username', 'email', 'profile_picture')