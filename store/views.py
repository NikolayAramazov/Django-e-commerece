import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from DjangoProject1 import settings
from storage.models import Product
from store.forms import CreateProductForm, CreateNewCategoryForm, EditProductForm
from store.models import Category, Ad


api_key = settings.EXCHANGE_RATE_API_KEY

def home(request):
    categories = Category.objects.all()
    ads = Ad.objects.filter(is_active=True)
    best_sellers = Product.objects.filter(stock__gt=0,sales__gt=0).order_by('-sales')[:10]
    on_sale_products = Product.objects.filter(stock__gt=0, is_on_sale=True).order_by('-stock')[:10]
    recently_viewed_ids = request.session.get('recently_viewed', [])
    recently_viewed_products = Product.objects.filter(id__in=recently_viewed_ids)
    recently_viewed_products = sorted(
        recently_viewed_products,
        key=lambda p: recently_viewed_ids.index(p.id)
    )

    return render(request, 'store/home.html', {'best_sellers': best_sellers,'categories': categories, 'ads': ads,'on_sale_products':on_sale_products, 'recently_viewed_products': recently_viewed_products})


def load_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'store/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    price = product.on_sale_price if product.is_on_sale else product.price

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] < product.stock:
            cart[str(product_id)]['quantity'] += 1
        else:
            pass
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(price),
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

def get_exchange_rates(request):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch exchange rates"}, status=500)

    data = response.json()
    return JsonResponse(data)

class CreateProductView(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    form_class = CreateProductForm
    template_name = 'store/create_product.html'
    success_url = reverse_lazy('store:home')

    def test_func(self):
        return self.request.user.is_superuser

class CreateCategoryView(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = Category
    form_class = CreateNewCategoryForm
    template_name = 'store/create_category.html'
    success_url = reverse_lazy('store:home')

    def test_func(self):
        return self.request.user.is_superuser

def load_ed_product_page(request):
    query = request.GET.get('query', '').strip()

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('store/edit_product_list_partial.html', {'products': products})
        return JsonResponse({'html': html})

    return render(request, 'store/ed_product_page.html', {'products': products, 'query': query})

class EditProductView(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    form_class = EditProductForm
    template_name = 'store/edit_product.html'
    success_url = reverse_lazy('store:home')
    pk_url_kwarg = 'product_id'

    def test_func(self):
        return self.request.user.is_superuser
