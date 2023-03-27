from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommissionForm
from .models import Commission


def commissions(request):
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():    
            form = form.save(commit=False)
            form.save()
            # return HttpResponseRedirect(reverse('home'))
            return render(request, 'commissions/post_submit_confirm.html',)
    else:
        form = CommissionForm()
    return render(request, 'commissions/commissions_form.html', {'form': form})