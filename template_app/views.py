from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request,"template_app/first.html")

def weatherview(request):
    weather_dic = {
    "Berlin": {
        "temperature": 22.5,  # Celsius
        "humidity": 60,  # Percentage
        "condition": "Partly Cloudy"
    },
    "Paris": {
        "temperature": 24.0,
        "humidity": 55,
        "condition": "Sunny"
    },
    "London": {
        "temperature": 18.2,
        "humidity": 70,
        "condition": "Rainy"
    },
    "NewYork": {
        "temperature": 27.8,
        "humidity": 65,
        "condition": "Sunny"
    },
    "Tokyo": {
        "temperature": 30.0,
        "humidity": 75,
        "condition": "Humid"
    },
    "Sydney": {
        "temperature": 21.5,
        "humidity": 68,
        "condition": "Clear"
    },
    "Istanbul": {
        "temperature": 29.0,
        "humidity": 50,
        "condition": "Sunny"
    },
    "Moscow": {
        "temperature": 16.0,
        "humidity": 80,
        "condition": "Cloudy"
    },
    "Beijing": {
        "temperature": 32.0,
        "humidity": 70,
        "condition": "Sunny"
    },
    "Delhi": {
        "temperature": 35.0,
        "humidity": 40,
        "condition": "Hot"
    },
    "user_premium" : True ,
    "username" : "Jean Jacques Rousseau" ,
    } 
    return render(request,"template_app/weather.html",context=weather_dic)