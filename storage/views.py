from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from storage.models import Product
from store.models import Category


def products_by_category(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'storage/product_list.html', {
        'products': products,
        'categories': categories,
    })


def all_products(request):
    query = request.GET.get('query', '').strip()

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('storage/product_list_partial.html', {'products': products})
        return JsonResponse({'html': html})

    return render(request, 'storage/product_list.html', {'products': products, 'query': query})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'storage/product_detail.html', {'product': product})
