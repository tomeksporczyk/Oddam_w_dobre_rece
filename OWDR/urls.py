from django.urls import path

from OWDR.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('login', LoginView.as_view(), name = 'login')
]
