
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.urls import path, reverse_lazy

from OWDR.views import LandingPageView, LoginView, LogoutView, RegisterView, UserProfileView, EditProfileView, \
    ChangePasswordView, FormView, MyDonationsView, DonationDetailsView, activate

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
    url(r'^user/reset/password/$',
        auth_views.PasswordResetView.as_view(template_name='OWDR/reset_password.html',
                                             success_url=reverse_lazy('user_reset_password_done')),
        name='user_reset_password'),
    url(r'^user/reset/password/done/$', auth_views.PasswordResetDoneView.as_view(), name='user_reset_password_done'),
    url(r'^user/reset/password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^user/reset/password/complete/$', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
