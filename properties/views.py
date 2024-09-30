from django.shortcuts import render, get_object_or_404
from .models import Property

# Create your views here.

def all_properties(request):
    """ A view to return all properties, including sorting and searching queries """

    properties = Property.objects.all()

    context = {
        'properties': properties
    }
    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """

    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }
    return render(request, 'properties/property_detail.html', context)