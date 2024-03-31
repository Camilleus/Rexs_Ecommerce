from django.shortcuts import render, redirect
from .models import Category, Customer, Product, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home_page(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_page(request):
    return render(request, 'product.html', {})


def about_page(request):
    return render(request, 'about.html', {})


def signin_page(request):
    messages.success(request, 'Signed in successfully')
    return render(request, 'signin.html', {})


def login_user_page(request):
    if request.method == 'POST': 
        login = request.POST.get('login_field')
        password = request.POST.get('password')
        user = authenticate(request, username=login, password=password) 
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user_page(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
