from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('all_properties'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H7S2yEXZJ64Aa3zH9yjBZ4Iy2ZgZKVOXOLuVAXjdhPHjai1xB870tMh2MtU3AizipzkItfXyD6U9nHQz5FXdyax00cSBMGuEP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)