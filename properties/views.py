from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Property, Category

# Create your views here.

def all_properties(request):
    """ A view to return all properties, including sorting and searching queries """

    properties = Property.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                properties = properties.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET: 
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  
            properties = properties.order_by(sortkey) 

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            properties = properties.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('properties'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            properties = properties.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'properties': properties,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """

    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }
    return render(request, 'properties/property_detail.html', context)