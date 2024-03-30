from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from weatherapp.models import Weather


def weather(request):
    return render(request, "weather.html")


def search(request):
    try:
        if request.method == 'POST':
            city_name = request.POST.get('city')
            API_KEY = '6440b74da23867d7cabf14b30f57a6bd'
            weather_API_url = (
                f'https://api.openweathermap.org/data/2.5/weather?q={city_name}'
                f'&units=metric&appid={API_KEY}'
            )

            response = requests.get(weather_API_url)
            weather_data = response.json()

            temperature = weather_data['main']['temp']
            weather_description = weather_data['weather'][0]['main']
            humidity = weather_data['main']['humidity']
            feels_like = weather_data['main']['feels_like']
            max_temp = weather_data['main']['temp_max']
            min_temp = weather_data['main']['temp_min']
            city = weather_data['name']
            weather_icon = weather_data['weather'][0]['icon']

            return render(
                request,
                "weather.html",
                {
                    'icon': weather_icon,
                    'temp': temperature,
                    'city': city_name,
                    'max_temp': max_temp,
                    'description': weather_description,
                    'humidity': humidity,
                    'feels_like': feels_like,
                    'min_temp': min_temp,
                    'city_name': city
                }
            )
    except KeyError:
        return render(request, 'error.html', {
            'message': 'Error retrieving weather data.'
            }
            )


def create(request):
    try:
        if request.method == 'POST':
            wthr = Weather()
            wthr.city = request.POST.get('city')
            wthr.save()
            return HttpResponseRedirect('/')
    except Weather.DoesNotExist:
        return render(request, 'error.html')


def main(request):
    weather_objects = Weather.objects.all()

    if not weather_objects.exists():
        return render(request, 'index.html', {
            'message': 'No cities found in Weather model.'
            }
        )

    for weather in weather_objects:
        city_name = weather.city

    try:
        weather_API_url = (
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}'
            '&units=metric&appid=6440b74da23867d7cabf14b30f57a6bd'
        )

        response = requests.get(weather_API_url)
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['main']
        humidity = weather_data['main']['humidity']
        feels_like = weather_data['main']['feels_like']
        max_temp = weather_data['main']['temp_max']
        min_temp = weather_data['main']['temp_min']
        city_name = weather_data['name']
        weather_icon = weather_data['weather'][0]['icon']

        return render(request, "index.html", {
            'data': weather_data,
            'icon': weather_icon,
            'temp': temperature,
            'description': description,
            'humidity': humidity,
            'feels_like': feels_like,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'city_name': city_name
        })
    except KeyError:
        return render(request, 'error.html', {
            'message': 'Error retrieving weather data.'
            }
        )
