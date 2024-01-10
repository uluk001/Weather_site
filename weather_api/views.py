# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django.shortcuts import get_object_or_404
from .services import (
    get_weather_data, fetch_weather_data_from_api,
    create_weather_data, delete_weather_data,
)
from django.conf import settings

OPENWEATHERMAP_API_KEY = settings.OPENWEATHERMAP_API_KEY

class WeatherDataAPIView(APIView):
    def get(self, request):
        city_name = self.request.query_params.get('city')
        
        weather_data = get_weather_data(city_name)

        if weather_data:
            serializer = WeatherDataSerializer(weather_data)
            return Response(serializer.data)
        
        api_key = OPENWEATHERMAP_API_KEY
        weather_api_data = fetch_weather_data_from_api(city_name, api_key)
        
        if weather_api_data:
            delete_weather_data(city_name)
            create_weather_data(city_name, **weather_api_data)
            weather_api_data.update({'city': city_name})
            return Response(weather_api_data)
        else:
            return Response({'error': 'Unable to fetch weather data from API'}, status=status.HTTP_400_BAD_REQUEST)