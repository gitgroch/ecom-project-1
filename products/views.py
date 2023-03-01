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

    # check if there is a request
    if request.GET:
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

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)