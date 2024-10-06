from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Property

# Create your views here.

def all_properties(request):
    """ A view to return all properties, including sorting and searching queries """

    properties = Property.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('properties'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            properties = properties.filter(queries)

    context = {
        'properties': properties,
        'search_term': query,
    }
    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """

    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }
    return render(request, 'properties/property_detail.html', context)