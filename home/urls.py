from django.urls import path
from . import views 




urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('productpage/<str:id_test>/', views.productpage, name='productpage'),
    path('test/', views.test, name='test'),
     path('oga/', views.oga, name='oga'),
    path('cart/', views.cart, name='cart'),
    path('create/', views.create, name='create'),
    


]