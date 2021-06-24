from django.forms import ModelForm, ValidationError
from geopy import Nominatim
import typing as t

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

    def clean_location(self) -> t.Any:
        location = self.cleaned_data.get('location')
        geolocator = Nominatim(user_agent='Mozilla/5.0')
        try:
            geolocator.geocode(location)
            return location
        except AttributeError:
            raise ValidationError('Неверный адрес')
