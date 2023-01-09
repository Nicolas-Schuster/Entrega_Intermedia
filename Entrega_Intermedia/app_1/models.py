from django.db import models

class Electrodomesticos(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()




class Tecnologia(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()


class Hogar(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()


class Herramientas(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()


class Indumentaria(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()


class Perfumeria(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()


class Automotor(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    shipping_cost= models.IntegerField()