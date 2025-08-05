from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('pay/<int:order_id>/', views.payment_view, name='payment'),
    path('complete_order/<int:order_id>/', views.complete_order, name='complete_order'),
    path('payment_failed', views.payment_failed, name='payment_failed'),
]