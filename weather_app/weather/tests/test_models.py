from django.test import TestCase, Client
from django.urls import reverse
from weather.models import City


class TestModels(TestCase):

    # def add_city(self):
    #     self.


    def test_city_name_correct(self):
        city1 = City.objects.create(name="San Fransisco")
        self.assertEquals(city1.name, "San Fransisco")

    def test_city_name_incorrect(self):
        city2 = City.objects.create(name="San Fransisco")
        self.assertNotEqual(city2.name, "LA") == False

        # self.assertTemplateUsed()
