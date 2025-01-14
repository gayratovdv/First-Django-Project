from django.shortcuts import render

def sign_up(request):
    return render(request, 'sign_up.html')


def login(request):
    return render(request, 'login.html')