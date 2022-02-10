from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from weatherapp.models import Weather
# Create your views here.

def main(request):
    return render(request, "index.html")

def weather(request):
        return render(request, "weather.html")

def search(request):
    try:
        if request.method == 'POST':
            city = request.POST.get('city')
            API_KEY = '6440b74da23867d7cabf14b30f57a6bd'
            weather_API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
            res = requests.get(weather_API)
            data = res.json()
            temp = data['main']['temp']
            discription = data['weather'][0]['main']
            humidity = data['main']['humidity']
            like = data['main']['feels_like']
            max = data['main']['temp_max']
            min = data['main']['temp_min']
            name = data['name']
            icon = data['weather'][0]['icon']
            return render(request, "weather.html", {'icon':icon, 'temp':temp, 'city':city, 'discription':discription, 'humidity':humidity, 'like':like, 'min':min, 'max':max, 'name':name})
    except KeyError:
        return render(request, 'error.html')


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
    try:
        weatherr = Weather.objects.all()
        for i in weatherr:
            strr = i.city
            print(strr)
        weather_API = f'https://api.openweathermap.org/data/2.5/weather?q={strr}&units=metric&appid=6440b74da23867d7cabf14b30f57a6bd'
        res = requests.get(weather_API)
        data2 = res.json()
        temp1 = data2['main']['temp']
        discription1 = data2['weather'][0]['main']
        humidity1 = data2['main']['humidity']
        like1 = data2['main']['feels_like']
        max1 = data2['main']['temp_max']
        min1 = data2['main']['temp_min']
        name1 = data2['name']
        return render(request, "index.html", {'data':data2, 'temp':temp1, 'discription':discription1, 'humidity':humidity1, 'like':like1, 'min':min1, 'max':max1, 'name':name1})
    except KeyError:
        return render(request, 'error.html')
# def main(request):
#     weatherr = Weather.objects.all()
#     return render(request, "index.html", {'weatherr':weatherr})
