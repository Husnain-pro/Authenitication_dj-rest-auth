from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import (PasswordChangeView, PasswordResetConfirmView,
                    PasswordResetView, UserDetailsView)

urlpatterns = [
    path('password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),

]
