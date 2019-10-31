from django import forms
from .models import Result
from . import scripts
from .scripts import main

class NewResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('city', 'country', 'spot_un', 'image', 'playlist', 'w_desc', 'temp', 'cloudy', 'humid', 'datetime')
        widgets = {'image': forms.HiddenInput(), 'playlist': forms.HiddenInput(), 'w_desc': forms.HiddenInput(), 'temp': forms.HiddenInput(),
        'cloudy': forms.HiddenInput(), 'humid': forms.HiddenInput(), 'datetime': forms.HiddenInput()}

    def clean(self): #cleans hidden field form data before being passed to view
        try:
            cleaned_data = super(NewResultForm, self).clean()
            city = cleaned_data['city']
            country = cleaned_data['country']
            username = cleaned_data['spot_un']
            cleaned_data['image'], cleaned_data['playlist'], cleaned_data['w_desc'], cleaned_data['temp'], cleaned_data['cloudy'], cleaned_data['humid'] = main.main(city,country,username)
            del self._errors['image']
            del self._errors['playlist']
            del self._errors['w_desc']
            del self._errors['temp']
            del self._errors['cloudy']
            del self._errors['humid']
            return cleaned_data
        except (TypeError):
            print('TypeError: Please check input data.')
            return
