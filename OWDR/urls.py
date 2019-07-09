from django.urls import path

from OWDR.views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('form', FormView.as_view(), name='form'),
    path('staff', StaffView.as_view(), name='staff'),
]
