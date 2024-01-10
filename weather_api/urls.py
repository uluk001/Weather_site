from .views import WeatherDataAPIView
from django.urls import path

urlpatterns = [
    path('', WeatherDataAPIView.as_view()),
]