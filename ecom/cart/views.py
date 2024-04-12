from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .cart import Cart
from store.models import Category, Product


categories = Category.objects.all()


def cart_page(request):
    cart = Cart(request)
    products = Product.objects.all()
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total_price = cart.get_total_price()
    return render(request, 'cart_summary.html', {'products': products, 'categories': categories, 'cart_products': cart_products, 'quantities': quantities, 'total_price': total_price})


def cart_add_page(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_count = len(cart)
        response_data = {
            'product_name': product.name,
            'cart_count': cart_count
        }
        return JsonResponse(response_data)


def cart_update_page(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.update(product=product, quantity=product_qty)
        cart_count = len(cart)
        response_data = {
            'product_name': product.name,
            'cart_count': cart_count
        }
        return JsonResponse(response_data)


def cart_delete_page(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.delete(product=product)
        cart_count = len(cart)
        response_data = {
            'product_name': product.name,
            'cart_count': cart_count
        }
        return JsonResponse(response_data)