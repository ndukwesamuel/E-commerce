from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import pppp




class createProduct(forms.ModelForm):
    class Meta:
        model = pppp
        fields = ['name', 'price', 'description', 'product_pic']