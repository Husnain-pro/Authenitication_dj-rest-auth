
from django.contrib import admin
from django.urls import include, path

from .views import ( PasswordChangeView,
                                PasswordResetConfirmView, PasswordResetView,
                                UserDetailsView)
from django.urls import path
from django.conf import settings

urlpatterns = [
      # URLs that do not require a session or valid token
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # path('^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
    # name='password_reset_confirm'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # URLs that require a user to be logged in with a valid session / token.
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

]

