from django.db import models

# Create your models here.

class Autos(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return self.marca

class Motos(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return self.marca


class Camiones(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return self.marca


class Aviones(models.Model):
    modelo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return self.modelo