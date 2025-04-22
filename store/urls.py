from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.load_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-one-piece/<int:product_id>/', views.add_one_piece, name='add_one_piece'),
]
