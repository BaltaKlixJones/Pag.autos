from django.db import models

# Create your models here.

class Autos(models.Model):
    marca= models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()


class Motos(models.Model):
    marca= models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()


class Camiones(models.Model):
    marca= models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()


class Aviones(models.Model):
    marca= models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    anio = models.IntegerField()

# otra cosa

class Vw(models.Model) :
    color = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()


class Bmw(models.Model) :
    color  = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()


class Mercedes(models.Model):
    color  = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()

class Ferrari(models.Model) :
    color  = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()

class Audi(models.Model) :
    color  = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()

class Lambo(models.Model) :
    color  = models.CharField(max_length=50)
    fabricacion = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()