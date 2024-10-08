from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    property_count = 0

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
