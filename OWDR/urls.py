
from django.conf.urls import url

from rest_framework import routers
from django.urls import path

from OWDR.views import LandingPageView, LoginView, LogoutView, RegisterView, UserProfileView, EditProfileView, ChangePasswordView, FormView, MyDonationsView, DonationDetailsView, activate

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('profile/edit', EditProfileView.as_view(), name='profile_edit'),
    path('profile/change-password', ChangePasswordView.as_view(), name='change_password'),
    path('form', FormView.as_view(), name='form'),
    path('donations/', MyDonationsView.as_view(), name='donation_list'),
    path('donations/<int:pk>', DonationDetailsView.as_view(), name='donation_details'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
