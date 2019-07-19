from rest_framework import routers
from django.urls import path, include

from OWDR.views import *

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
]
