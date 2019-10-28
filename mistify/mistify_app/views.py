from django.shortcuts import render, redirect, get_object_or_404
import os
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from . import scripts
from .scripts import main

# Create your views here.

w_key = os.environ.get('WEATHER_KEY')

@login_required
def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        place.user = request.user
        if form.is_valid():
            main(place.city,place.country)
            place.save()
            return redirect('place_list')

    places = Place.objects.filter(user=request.user).order_by('country')
    places = places.order_by('city')
    new_place_form = NewPlaceForm()
    return render(request, 'mistify_app/mistify.html', {'places': places, 'new_place_form': new_place_form})

@login_required
def stored_result(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    return render(request, 'mistify_app/stored_result.html', {'place': place} )

@login_required
def delete_result(request):
    pk = request.POST.get('pk')
    place = get_object_or_404(Place, pk=pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()
