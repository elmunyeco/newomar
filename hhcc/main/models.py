# main/models.py
from django.db import models

class HistoriaClinica(models.Model):
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero} - {self.nombre} {self.apellido}"
