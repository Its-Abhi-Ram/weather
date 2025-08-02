from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    city = request.GET.get('city', 'bangalore')
    api_key = '03b1acbfd0387ac994dad57eb102fe01'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # print(api_url)
  

    api = requests.get(api_url).json()
    temp = api['main']['temp']
    country  = api['sys']['country']
    city = api['name']
    weather = api['weather'][0]['main']
    description = api['weather'][0]['description']
    humidity = api['main']['humidity']
    wind_speed = api['wind']['speed']


    ctx = {"temp": temp, "country": country, "city":city, "weather": weather, "description": description, "humidity": humidity, "wind_speed": wind_speed}
    
    return render(request, 'index.html', ctx)