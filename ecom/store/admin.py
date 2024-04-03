from django.contrib import admin
from .models import Category, Product, Order, Customer, Profile, create_profile, Meep

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)