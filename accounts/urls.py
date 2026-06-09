from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('register/', views.register, name='register'),
    path('check_email/', views.check_email, name='check_email'),
    path('email_confirm/', views.email_confirm, name='email_confirm'),
    path('logout/', views.sign_out, name='logout'),
]