from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('pay/<int:order_id>/', views.payment_view, name='payment'),
    path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
]