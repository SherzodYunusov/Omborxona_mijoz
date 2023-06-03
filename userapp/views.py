from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Asosiy.models import *



def home(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/bolim/")
    return render(request, 'home.html')

def logout1(request):
    logout(request)
    return redirect('/')



# Create your views here.
