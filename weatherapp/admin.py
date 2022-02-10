from django.contrib import admin

from weatherapp.models import Weather

# Register your models here.
class WeatherAdmin(admin.ModelAdmin):
    list_display = ("id", "city")

admin.site.register(Weather, WeatherAdmin)