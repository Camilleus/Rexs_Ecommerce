from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product/<int:pk>', views.product_page, name='product'),
    path('product_category/<int:pk>', views.product_category_page, name='product_category'),
    path('about/', views.about_page, name='about'),
    path('signup/', views.signup_user_page, name='signup'),
    path('login/', views.login_user_page, name='login'),
    path('logout/', views.logout_user_page, name='logout'),
]
