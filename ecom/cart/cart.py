from decimal import *


from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True


    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        return products
        
    
    def get_quants(self):
        quantities = self.cart
        return quantities
        
        
    def update(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
        self.session.modified = True


    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        
    def get_total_price(self):
        total = 0
        quantities = self.get_quants()
        for product_id, quantity in quantities.items():
            product = Product.objects.get(id=product_id)
            total += int(quantity) * float(product.price)
        return total