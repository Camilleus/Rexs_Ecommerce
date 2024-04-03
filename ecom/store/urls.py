from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product/<int:pk>', views.product_page, name='product'),
    path('category/<str:foo>', views.category_page, name='category'),
    path('category/<str:category_name>/', views.category_page, name='category1'),
    path('about/', views.about_page, name='about'),
    path('signup/', views.signup_user_page, name='signup'),
    path('login/', views.login_user_page, name='login'),
    path('logout/', views.logout_user_page, name='logout'),
]
