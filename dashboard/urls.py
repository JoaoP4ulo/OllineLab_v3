from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lab1/', views.lab1, name='lab1'),
    path('lab2/', views.lab2, name='lab2'),
    path('lab3/', views.lab3, name='lab3'),
    path('ler_temperatura/', views.ler_temperatura, name='ler_temperatura'),
    path('valor_temp', views.valor_temp, name='valor_temp'),
    
]