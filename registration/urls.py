from django.urls import path

from registration.views import sign_up, login

app_name = 'registration'

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', login, name='login')
]
