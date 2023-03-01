from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # check if there is a request
    if request.GET:
        # Check if sort is in request.GET
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            # Check if sortkey is equal to category
            if sortkey == 'category':
                sortkey = 'category__name'
            # Check for direction 
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        # Check for category query in request
        if 'category' in request.GET:
            # If exists convert to list 
            categories = request.GET['category'].split(',')
            # filter down to products in the list
            products = products.filter(category__name__in=categories)
            # filter categories
            categories = Category.objects.filter(name__in=categories)

        # check if text inport (q) is in request.GET
        if 'q' in request.GET:
            # Set to variable query
            query = request.GET['q']
            # response if query blank, redirect to products
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # defining queries variable
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,    
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)