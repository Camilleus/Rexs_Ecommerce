from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from .models import Category, Customer, Product, Order
from .forms import ProfilePicForm, MeepForm, SignUpForm


def home_page(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_page(request, pk):
    product = get_object_or_404(Product, id=pk)
    related_products = Product.objects.filter(category__name=product.category.name).exclude(id=pk)
    return render(request, 'product.html', {'product': product, 'related_products': related_products})


def category_page(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = get_object_or_404(Category, name=foo)
        products = Product.objects.filter(category=category)
        categories = Category.objects.all()
        return render(request, 'category.html', {'category': category, 'categories': categories, 'products': products})
    except:
        messages.success(request, 'Whoops! This Category does not exist!')
        return redirect('home')


def about_page(request):
    return render(request, 'about.html', {})


def signup_user_page(request):
    form = SignUpForm()
    if request.method == 'POST': 
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully signed up! Welcome!')
            return redirect('home')
        else:
            messages.success(request, 'Whoops! There was an error signin up, please try again')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})


def login_user_page(request):
    if request.method == 'POST': 
        login_c = request.POST['login_field']  
        password = request.POST['password']
        user = authenticate(request, username=login_c, password=password) 
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
