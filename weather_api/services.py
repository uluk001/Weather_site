from .models import WeatherData
from datetime import datetime, timedelta
from django.utils import timezone
import requests


def get_weather_data(city_name):
    try:
        return WeatherData.objects.get(city=city_name, timestamp__gte=(timezone.now() - timedelta(minutes=30)))
    except WeatherData.DoesNotExist:
        return None


def fetch_weather_data_from_api(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        
        return {
            'temperature': temperature,
            'pressure': pressure,
            'wind_speed': wind_speed,
        }
    else:
        return None


def create_weather_data(city_name, temperature, pressure, wind_speed):
    WeatherData.objects.create(city=city_name, temperature=temperature, pressure=pressure, wind_speed=wind_speed)


def delete_weather_data(city_name):
    WeatherData.objects.filter(city=city_name).delete()
