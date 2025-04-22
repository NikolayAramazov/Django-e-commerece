from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from storage.models import Product
from store.models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'categories': categories})


def load_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'store/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] < product.stock:
            cart[str(product_id)]['quantity'] += 1
        else:
            pass
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'stock': product.stock,
        }

    request.session['cart'] = cart
    return redirect('store:cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            del cart[str(product_id)]

    request.session['cart'] = cart

    return render(request, 'store/cart.html', {'cart': cart})


def add_one_piece(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] < product.stock:
            cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'stock': product.stock,
        }

    request.session['cart'] = cart

    return redirect('store:cart')
