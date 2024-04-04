from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart_page'),
    path('add/', views.cart_add_page, name='cart_add_page'),
    path('delete/', views.cart_delete_page, name='cart_delete_page'),
    path('update/', views.cart_update_page, name='cart_update_page')
]
