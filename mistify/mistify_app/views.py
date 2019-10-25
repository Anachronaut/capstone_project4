from django.shortcuts import render, redirect
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            return redirect('place_list')


    new_place_form = NewPlaceForm()
    return render(request, 'mistify_app/mistify.html', {'new_place_form': new_place_form})
