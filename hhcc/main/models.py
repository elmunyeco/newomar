# main/models.py
from django.db import models

class HistoriaClinica(models.Model):
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    afiliado = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    enfermedades = models.ManyToManyField('Enfermedad')

    def __str__(self):
        return f"{self.numero} - {self.nombre} {self.apellido}"

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    
class SignosVitales(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    colesterol = models.DecimalField(max_digits=5, decimal_places=2)
    glucemia = models.DecimalField(max_digits=5, decimal_places=2)
    presionSistolica = models.DecimalField(max_digits=3, decimal_places=0)
    presionDiastolica = models.DecimalField(max_digits=3, decimal_places=0)
