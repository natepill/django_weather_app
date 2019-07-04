

'''

from django.test import TestCase, Client
from django.urls import reverse
from weather.models import City


class TestViews(TestCase):

    def test_index_GET(self):
        client = Client()
        client.get(reverse('weather_page'))
        self.assertEquals(response.status_code, 200)


        # self.assertTemplateUsed()
'''
