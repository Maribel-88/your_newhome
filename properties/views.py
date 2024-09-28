from django.shortcuts import render
from .models import Property

# Create your views here.

def all_properties(request):
    """ A view to return all properties, including sorting and searching queries """

    properties = Property.objects.all()

    context = {
        'properties': properties
    }
    return render(request, 'properties/properties.html', context)
