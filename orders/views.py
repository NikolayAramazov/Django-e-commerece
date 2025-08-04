from django.utils import timezone
from django.shortcuts import render, redirect
from DjangoProject1 import settings
from orders.forms import CheckoutForm
from orders.models import Order, Address, Payment
import stripe
from storage.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            session_cart = request.session.get('cart', {})
            total_price = 0
            cart_items = []

            for product_id, item in session_cart.items():
                try:
                    product = Product.objects.get(id=product_id)
                    quantity = item['quantity']
                    total_price += product.price * quantity
                    cart_items.append((product, quantity))
                except Product.DoesNotExist:
                    continue

            if total_price == 0:
                return redirect('cart')

            address = Address.objects.create(
                user=request.user,
                full_name=data['full_name'],
                phone=data['phone'],
                address_line=data['address_line'],
                city=data['city'],
                zip_code=data['zip_code'],
                is_billing=True
            )

            order = Order.objects.create(
                user=request.user,
                address=address,
                is_paid=False,
                total_price=total_price
            )

            request.session.modified = True

            return redirect('orders:payment', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {'form': form})


def payment_view(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=int(order.total_price * 100),
                currency='usd',
                description=f'Order #{order.id}',
                source=token,
            )

            Payment.objects.create(
                order=order,
                status='Paid',
                paid_at=timezone.now()
            )

            order.is_paid = True
            order.save()

            return redirect('orders:complete_order', order_id=order.id)
        except stripe.error.CardError as e:
            return render(request, 'orders/payment_failed.html', {'error': str(e)})

    context = {
        'order': order,
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'orders/payment.html', context)


def complete_order(request,order_id):
    order = Order.objects.get(id=order_id)

    if order.status == 'Completed':
        return render(request, 'orders/complete_order.html', {'order': order})

    session_cart = request.session.get('cart', {})

    for product_id, item in session_cart.items():
        product = Product.objects.get(id=product_id)
        quantity = item['quantity']

        if product.stock >= quantity:
            product.stock -= quantity
            product.sales += quantity
            product.save()

    order.status = 'Completed'
    order.save()

    request.session['cart'] = {}
    request.session.modified = True

    return render(request, 'orders/complete_order.html', {'order': order})