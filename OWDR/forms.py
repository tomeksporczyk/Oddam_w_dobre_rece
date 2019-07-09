from django import forms


class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=64, label='E-mail')
    user_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Hasło')

