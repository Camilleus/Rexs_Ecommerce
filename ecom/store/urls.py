from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product/', views.product_page, name='product'),
    path('about/', views.about_page, name='about'),
]
