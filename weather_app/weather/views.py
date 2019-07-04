from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=579ada901351c01b78b7df86d0346581'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    # print(request.text)
    cities = City.objects.all()


    weather_data = []

    for city in cities:

        weather_request = requests.get(url.format(city)).json()



        city_weather = {
            'city' : city.name,
            'temperature' : weather_request['main']['temp'],
            'description' : weather_request['weather'][0]['description'],
            'icon' : weather_request['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)
