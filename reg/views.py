from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, login
from django.contrib.auth.decorators import login_required
from django.contrib import  messages


# Create your views here.
from django.contrib.auth.models import  User

# from  signin.form import  CreateUserForm
from  reg.form import  CreateUserForm


def account(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     form = CreateUserForm()
    #     if request.method == 'POST':
    #         form = CreateUserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             user = form.cleaned_data.get('username')
    #             print(user)
    #             messages.success(request, 'Account was created for user: ' +user+ ' click login')
    #             return redirect('account')
    #         else:
    #             bad = form.errors
    #             print(bad)
    #             context = {'bad': bad}
    #     context = {'form':form,}
    return render(request, 'account.html', {}) 


# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password1')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Account was created for user: ' +user+ ' click login')
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Password or username not correct')
                
#         return render(request, 'account.html',) 

