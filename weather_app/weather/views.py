from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=579ada901351c01b78b7df86d0346581'
    city = 'san francisco'

    city_weather = {
        'city' : city,
        'temperature' : weather_request['main']['temp'],
        'description' : weather_request['weather'][0]['description'],
        'icon' : weather_request['weather'][0]['icon'],
    }

    # print(request.text)

    weather_data = []

    for city in cities:

        weather_request = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        
        weather_data.append(city_weather)

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
