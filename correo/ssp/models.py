from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Service(models.Model):
    id_service = models.SmallAutoField(primary_key=True)
    name_service = models.CharField(max_length=100)
    cost_service = models.FloatField()

    def __str__(self):
        return str(self.name_service)


class Zone(models.Model):
    id_zone = models.IntegerField(primary_key=True)
    name_zone = models.CharField(max_length=100)
    # ! valores iguales, cuando los agregauemos en el admin
    zone_position = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name_zone)


class neighborhood(models.Model):
    name_neighbor = models.CharField(max_length=100)
    zone_neighbor = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_neighbor


class Person(models.Model):
    type_per = [
        ('NT', 'Natural'),
        ('LG', 'Legal'),
    ]

    name_person = models.CharField(max_length=200)
    identification_name = models.CharField(max_length=100, unique=True)
    phone_person = models.BigIntegerField(blank=True)
    type_person = models.CharField(max_length=100, choices=type_per)
    neighbor_person = models.ForeignKey(neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.identification_name


class Courier(models.Model):
    id_courier = models.AutoField(primary_key=True)
    name_courier = models.CharField(max_length=200)
    identification_courier = models.CharField(max_length=100, unique=True)
    phone_courier = models.BigIntegerField()
    last_location = models.CharField(max_length=100)
    available_courier = models.BooleanField()

    def __str__(self):
        return self.name_courier



class PackageSending(models.Model):
    status = [
        ('pkp', 'Pick up'),
        ('ow', 'On the way'),
        ('dlv', 'Delivered'),
        ('Rtd', 'Returned'),
        ('err', 'With error')
    ]
    id_sending = models.AutoField(primary_key=True)
    date_sending = models.DateTimeField('Fecha de envio', auto_now=True)
    date_delivery = models.DateTimeField('Fecha de llegada estimada', blank=True, auto_now=True)
    status_delivery = models.CharField(max_length=30, choices=status, default='pkp')
    address_pickup = models.CharField(max_length=200)
    address_delivery = models.CharField(max_length=200)
    cost_sending = models.FloatField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    assigned_courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    pickup_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='pickup')
    delivery_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='delivery')
    sender_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender')
    receiver_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return str(self.id_sending)




