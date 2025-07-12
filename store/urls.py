from django.urls import path
from . import views
from .views import CreateProductView, CreateCategoryView, EditProductView

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.load_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-one-piece/<int:product_id>/', views.add_one_piece, name='add_one_piece'),
    path('api/exchange-rates/', views.get_exchange_rates, name='exchange_rates'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('ed_product_page/', views.load_ed_product_page, name='ed_product_page'),
    path('edit_product/<int:product_id>/', EditProductView.as_view(), name='edit_product'),
]
