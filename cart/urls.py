from django.shortcuts import render
from django.urls import path
from cart import views

# Create your views here.
app_name='cart'
urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/', views.AddtoCart, name='AddtoCart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('remove_all/<int:product_id>/', views.remove_all, name='remove_all'),

]