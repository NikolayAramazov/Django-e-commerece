from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('products/category/', views.products_by_category, name='products_by_category'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]