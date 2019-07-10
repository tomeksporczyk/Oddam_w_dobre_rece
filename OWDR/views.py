from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from OWDR.forms import *


class LandingPageView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'OWDR/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'OWDR/login.html', context={'form': LoginForm().as_p()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_login')
            user_password = form.cleaned_data.get('user_password')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                next_ = request.GET.get('next')
                print(user.is_staff)
                if next_ is not None:
                    if user.is_staff:
                        next_ = reverse_lazy('staff')
                    return redirect(next_)
                else:
                    return redirect(reverse_lazy('landing_page'))
            else:
                message = 'Niepoprawne dane logowania'
                return render(request, 'OWDR/login.html', context={'form': LoginForm(), 'message': message})


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm().as_p()
        context = {'form': form}
        return render(request, 'OWDR/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        else:
            context = {'form': form}
            return render(request, 'OWDR/register.html', context)


class UserProfileView(View):
    def get(self, request):
        return render(request, 'OWDR/user_profile.html', context={'user': request.user})


class FormView(View):
    def get(self, request):
        return render(request, 'OWDR/form.html')


class StaffView(View):
    def get(self, request):
        return HttpResponse('staff')