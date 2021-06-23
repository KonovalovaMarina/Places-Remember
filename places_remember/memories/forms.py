from django.forms import ModelForm, ValidationError
from geopy import Nominatim

from .models import Memory


class AddMemoryForm(ModelForm):

    class Meta:
        model = Memory
        fields = ('location', 'title', 'description')
        labels = {
            'location': 'Координаты',
            'title': 'Заголовок',
            'description': 'Описание'
        }

    def clean_location(self):
        location = self.cleaned_data.get('location')
        geolocator = Nominatim(user_agent='Mozilla/5.0')
        try:
            place = geolocator.geocode(location)
            p_lat, p_lon = place.latitude, place.longitude
            return location
        except AttributeError:
            raise ValidationError('Неверный адрес')
