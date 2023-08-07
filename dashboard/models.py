from django.db import models
import datetime

class GetTemperatura(models.Model):
    valor = models.IntegerField()
    hora = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self) -> str:
        return str(self.valor)
    
class SetTemperatura(models.Model):
    set_on = models.BooleanField(default=False)
    max_temp = models.IntegerField(default=40)
    hora = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self) -> str:
        return self.max_temp