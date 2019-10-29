from django.shortcuts import render, redirect, get_object_or_404
from django import forms
import os
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def place_list(request):
    image_URL = 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Mist_and_Mountains_2_-_Mount_Abu.jpg'
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save(commit=False)
        place.user = request.user
        image_URL = place.image
        playlist_uri = place.playlist
        w_desc = place.w_desc
        temp = place.temp
        cloudy = place.cloudy
        humidity = place.humid
        if form.is_valid():
            place.save()
            places = Place.objects.filter(user=request.user).order_by('country')
            places = places.order_by('city')
            new_place_form = NewPlaceForm()
            return render(request, 'mistify_app/mistify.html', {'places': places, 'new_place_form': new_place_form, 'bg_url': image_URL, 'playlist_uri': playlist_uri, 'w_desc': w_desc, 'temp': temp,
            'cloudy': cloudy, 'humidity': humidity})
    places = Place.objects.filter(user=request.user).order_by('country', 'city')
    new_place_form = NewPlaceForm()
    return render(request, 'mistify_app/mistify.html', {'places': places, 'new_place_form': new_place_form, 'bg_url': image_URL})

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
