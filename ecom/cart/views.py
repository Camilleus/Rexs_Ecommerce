from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


from .cart import Cart
from store.models import Category, Product


categories = Category.objects.all()


def cart_page(request):
    products = Product.objects.all()
    return render(request, 'cart_summary.html', {'products': products, 'categories': categories})

def cart_add_page(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product) 
        cart_count = len(cart)
        response_data = {
            'product_name': product.name,
            'cart_count': cart_count
        }
        return JsonResponse(response_data)

def cart_update_page(request): 
    pass

def cart_delete_page(request):
    pass

