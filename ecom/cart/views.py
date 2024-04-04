from django.shortcuts import render


from ecom.store.models import Category, Product


categories = Category.objects.all()


def cart_page(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})

def cart_add_page(request):
    pass

def cart_update_page(request): 
    pass

def cart_delete_page(request):
    pass

