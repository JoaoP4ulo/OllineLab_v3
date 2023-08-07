from django.shortcuts import render
from .models import SetTemperatura, GetTemperatura
from django.http import JsonResponse
import datetime

def home(request):
    return render(request,'home.html')

def lab1(request):
    return render(request,'lab1.html')

def lab2(request):
    return render(request,'lab2.html')

def lab3(request):
    return render(request,'lab3.html')

def ler_temperatura(request):
    temperatura = GetTemperatura.objects.values_list('valor', flat=True)
    list_temp = list(temperatura)
    list_temperatura = list_temp[-10:]
    data_json = {'temperatura': list_temperatura,'labels':['','','','','','','','','','']}
    return JsonResponse(data_json)

def valor_temp(request):
    temperatura = GetTemperatura.objects.values_list('valor', flat=True)
    list_temp = list(temperatura)
    temp_atual = list_temp[-1]
    return JsonResponse({'temp_atual':temp_atual})