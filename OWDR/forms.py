from django import forms
from django.contrib.auth.forms import UserCreationForm

from OWDR.models import User


class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=64, label='E-mail')
    user_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Hasło')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')