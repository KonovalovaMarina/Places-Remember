from django.test import TestCase
from ..forms import AddMemoryForm


class AddMemoryFormTestCase(TestCase):

    def test_place_is_wrong(self):
        data = {
            'location': 'Несуществующее место',
            'title': 'Название',
            'description': 'Описание'
        }
        form = AddMemoryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_null_title(self):
        data = {
            'location': 'Екатеринбург, Тургенева 4',
            'title': '',
            'description': 'Описание'
        }
        form = AddMemoryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_null_description(self):
        data = {
            'location': 'Екатеринбург, Тургенева 4',
            'title': 'Название',
            'description': ''
        }
        form = AddMemoryForm(data=data)
        self.assertFalse(form.is_valid())
