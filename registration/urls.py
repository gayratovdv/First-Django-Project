from django.urls import path

from registration.views import sign_up

app_name = 'sign-up'

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up '),
]
