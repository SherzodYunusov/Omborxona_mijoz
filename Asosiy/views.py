from django.shortcuts import render, redirect
from .models import *
from userapp.models import Ombor
def client(request):
    if request.user.is_authenticated:
        content = {
            "mijoz": Mijoz.objects.filter(ombor1 = Ombor.objects.get(user = request.user))
        }
        return render(request, 'clients.html', content)
    return redirect('/')

def bolimlar(request):
    if request.user.is_authenticated:
        return render(request, 'bulimlar.html')
    return redirect('/')

def client_update(request):
    return render(request, 'client_update.html')

def product_update(request):
    return render(request, 'product_update.html')

def products(request):
    if request.method == 'POST':
        Mahsulot.objects.create(ombor1 = Ombor.objects.get(user = request.user),
            nom = request.POST['nom'],
            brend = request.POST['brend'],
            narx = request.POST['narx'],
            miqdor = request.POST['miqdor'],
            olchov = request.POST['olchov'],
            sana = request.POST['sana'],
            )
        return redirect('/product/')
    if request.user.is_authenticated:
        content = {
            'mahsulot': Mahsulot.objects.filter(ombor1 = Ombor.objects.get(user = request.user))
        }
        return render(request, 'products.html', content)
    return redirect('/')

def stats(request):
    if request.user.is_authenticated:
        return render(request, 'stats.html')
    return redirect('/')
# Create your views here.
