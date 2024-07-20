from django.urls import path
from . import views

app_name = "template_app"


urlpatterns = [
    path('',views.index, name="MainPage"),
    path('weather/', views.weatherview , name="Weather")
]