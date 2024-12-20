from django import forms
from django.contrib.auth.models import User
from .models import Room

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']

