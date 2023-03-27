from django.shortcuts import render
from .forms import CommissionForm
from .models import Commission


# Create your views here.
def commissions(request):
    """ A view to return the commissions form page """
    form = CommissionForm()
    return render(request, 'commissions/commissions_form.html', {'form': form})

