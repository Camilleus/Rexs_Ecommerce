from decimal import *


from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart


    def add(self, product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] += 1
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': 1}
            
        self.session.modified = True


    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())


    def get_prods(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        return products
        
        
    def get_product_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item