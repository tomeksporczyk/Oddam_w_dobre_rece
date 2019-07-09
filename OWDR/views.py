from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from OWDR.forms import *


class LandingPageView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'OWDR/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'OWDR/login.html', context={'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_login')
            user_password = form.cleaned_data.get('user_password')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                next_ = request.GET.get('next')
                if next_ is not None:
                    return redirect(next_)
                else:
                    return redirect(reverse_lazy('landing_page'))
            else:
                message = 'Niepoprawne dane logowania'
                return render(request, 'OWDR/login.html', context={'form': LoginForm(), 'message': message})


class RegisterView(View):
    def get(self, request):
        return render(request, 'OWDR/register.html')


class FormView(View):
    def get(self, request):
        return render(request, 'OWDR/form.html')
