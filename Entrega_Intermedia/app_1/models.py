from django.db import models

class Electrodomesticos(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()




class Tecnologia(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()


class Hogar(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()


class Herramientas(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()


class Indumentaria(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()


class Perfumeria(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()


class Automotor(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.FloatField()