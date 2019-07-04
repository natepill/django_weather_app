from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=579ada901351c01b78b7df86d0346581'
    city = 'san francisco'

    weather_request = requests.get(url.format(city)).json

    city_weather = {
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(weather_request.text)
    return render(request, 'weather/weather.html')
