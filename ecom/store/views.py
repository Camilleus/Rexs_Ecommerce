from django.shortcuts import render
from .models import Category, Customer, Product, Order



def home_page(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_page(request):
    return render(request, 'product.html', {})


def about_page(request):
    return render(request, 'about.html', {})
