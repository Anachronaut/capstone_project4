from django.shortcuts import render, redirect, get_object_or_404
from django import forms
import os
from .models import Result
from .forms import NewResultForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_form(request): #landing page form
    #default background image
    image_URL = 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Mist_and_Mountains_2_-_Mount_Abu.jpg'
    if request.method == 'POST':
        form = NewResultForm(request.POST)
        try:
            result = form.save(commit=False)
            result.user = request.user
            #form data
            image_URL = result.image
            playlist_uri = result.playlist
            w_desc = result.w_desc
            temp = result.temp
            cloudy = result.cloudy
            humidity = result.humid
            if form.is_valid():
                result.save()
                results = Result.objects.filter(user=request.user).order_by('country', 'city')
                new_result_form = NewResultForm()
                return render(request, 'mistify_app/mistify.html', {'results': results, 'new_result_form': new_result_form, 'bg_url': image_URL, 'playlist_uri': playlist_uri, 'w_desc': w_desc, 'temp': temp,
                'cloudy': cloudy, 'humidity': humidity})
        except (ValueError):
            print('ValueError: Please check input data.')
            return homeformReroute(request, image_URL)

    return homeformReroute(request, image_URL)

@login_required
def homeformReroute(request, image_URL): #reroutes to blank home_form
    results = Result.objects.filter(user=request.user).order_by('country', 'city')
    new_result_form = NewResultForm()
    return render(request, 'mistify_app/mistify.html', {'results': results, 'new_result_form': new_result_form, 'bg_url': image_URL})

@login_required
def stored_result(request, result_pk): #page for bookmarked results (location, playlist, weather, image)
    result = get_object_or_404(Result, pk=result_pk)
    image_URL = result.image
    playlist_uri = result.playlist
    w_desc = result.w_desc
    temp = result.temp
    cloudy = result.cloudy
    humidity = result.humid
    return render(request, 'mistify_app/stored_result.html', {'result': result, 'bg_url': image_URL, 'playlist_uri': playlist_uri, 'w_desc': w_desc, 'temp': temp,
    'cloudy': cloudy, 'humidity': humidity})

@login_required
def delete_result(request): #view for delete button
    pk = request.POST.get('pk')
    result = get_object_or_404(Result, pk=pk)
    if result.user == request.user:
        result.delete()
        return redirect('home_form')
    else:
        return HttpResponseForbidden()
