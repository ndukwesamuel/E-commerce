from django.shortcuts import render, redirect

from django.http import HttpResponseNotFound
from django.contrib.auth.models import  User

from home.models import pppp

from home.forms import createProduct

# Create your views here.





def home(request):

    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def product(request):
    product = pppp.objects.all()

    
    for i in product:
        print(i.description)

    context={'product':product}
 

    return render(request, 'product.html', context)

def productpage(request,id_test):
    single = pppp.objects.get(id=id_test)

    print(single.name)
    print(single.description)

    context= {"single": single}

    return render(request, 'productpage.html', context)


# def account(request):
    
#     return render(request, 'account.html', {})


def cart(request):

    return render(request, 'cart.html', {})


def oga(request):
    product = pppp.objects.all()


    context={'product':product}
    return render(request, 'adminroom.html', context)


def test(request):

    product = pppp.objects.all()

    
    for i in product:
        print(i.description)

    context={'product':product}
    return render(request, 'test.html', context)

def create(request):
    form = createProduct()
    if request.method == 'POST':
        print('posting POST ', request.POST)
        form =createProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('oga') 
        else:
            bad = form.errors
            print(bad)
            context = {'bad': bad}

    context={"form": form}

    return render(request, 'create.html', context )
# this area is for registration form

    





