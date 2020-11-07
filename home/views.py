from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def product(request):
    return render(request, 'product.html', {})

def productpage(request):

    return render(request, 'productpage.html', {})


def account(request):
    
    return render(request, 'account.html', {})


def cart(request):

    return render(request, 'cart.html', {})




