from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User, Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['nome', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)