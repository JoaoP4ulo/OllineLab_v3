from django.shortcuts import render
from .models import SetTemperatura, GetTemperatura
from django.http import JsonResponse
import datetime
import pyrebase
import pandas as pd

config={
    "apiKey": "AIzaSyCKS7ouEvn4bP0Bxalemw0GuHK6yWLbQhs",
    "authDomain": "onlinelab-dfd7c.firebaseapp.com",
    "databaseURL": "https://onlinelab-dfd7c-default-rtdb.firebaseio.com",
    "projectId": "onlinelab-dfd7c",
    "storageBucket": "onlinelab-dfd7c.appspot.com",
    "messagingSenderId": "436743910653",
    "appId": "1:436743910653:web:7f755bdc16f82e16b2fa94"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def ler_temperatura(request):
    agora = datetime.datetime.now()
    dia_atual = agora.strftime("%Y-%m-%d")
    hora_atual = agora.strftime("%H:%M:%S")
    time = f'{dia_atual} : {hora_atual}'
    # temperatura = GetTemperatura.objects.values_list('valor', flat=True)
    # list_temp = list(temperatura)
    # list_temperatura = list_temp[-10:]
    list_temperatura = [0,0,0,0,0,0,0,0,0,0]

    data = database.child('GetTemperatura').child('data').get().val()
    valor = database.child('GetTemperatura').child('valor').get().val()
    set = database.child('GetTemperatura').child('set').get().val()

    list_temperatura.append(valor)
    list_temperatura.pop(0)

    with open(f"datareading.csv", 'r+') as arquivo:
        arquivo.write(list_temperatura)

    data_json = {'temperatura': list_temperatura,'labels':['','','','','','','','','','']}
    return JsonResponse(data_json)

def valor_temp(request):
    # temperatura = GetTemperatura.objects.values_list('valor', flat=True)
    # list_temp = list(temperatura)
    # temp_atual = list_temp[-1]
    temp_atual = database.child('GetTemperatura').child('valor').get().val()
    return JsonResponse({'temp_atual':temp_atual})

def home(request):
    return render(request,'home.html')

def lab1(request):
    return render(request,'lab1.html')

def lab2(request):
    return render(request,'lab2.html')

def lab3(request):
    return render(request,'lab3.html')
