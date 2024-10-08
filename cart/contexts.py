from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from properties.models import Property

def cart_contents(request):

    cart_items = []
    total = 0
    property_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        property = get_object_or_404(Property, pk=item_id)
        total += quantity * property.price
        property_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'property': property,
        })

    if total < settings.FREE_BOOKING_THRESHOLD:
        booking_fee = total * Decimal(settings.STANDARD_BOOKING_PERCENTAGE/100)
        free_booking_delta = settings.FREE_BOOKING_THRESHOLD - total
    else:
        booking_fee = 0
        free_booking_delta = 0

    grand_total = booking_fee + total


    context = {
        'cart_items': cart_items,
        'total': total,
        'property_count': property_count,
        'booking_fee': booking_fee,
        'free_booking_delta': free_booking_delta,
        'free_booking_threshold': settings.FREE_BOOKING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
