from django.shortcuts import render

# Create your views here.
def commissions(request):
    """ A view to return the index page """
    return render(request, 'commissions/commissions_form.html')