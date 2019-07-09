from django.shortcuts import render

# Create your views here.
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'OWDR/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'OWDR/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'OWDR/register.html')


class FormView(View):
    def get(self, request):
        return render(request, 'OWDR/form.html')
