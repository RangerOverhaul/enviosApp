from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Service(models.Model):
    id_service = models.IntegerField(primary_key=True)
    type_service = models.CharField(max_length=100)
    cost_service = models.FloatField()

    def __str__(self):
        return str(self.type_service)


class neighborhood(models.Model):
    name_neighbor = models.CharField(max_length=100)
    # Codigo especial del barrio
    neigh_id = models.IntegerField(primary_key=True)
    # codigo del barrio en que esta
    zone_id = models.CharField(max_length=4, blank=True, null=True)
    def __str__(self):
        return self.name_neighbor


class Zone(models.Model):
    zone_id = models.IntegerField(primary_key=True)
    neighborhoods = models.ForeignKey(neighborhood, on_delete=models.CASCADE)
    # ! valores iguales, cuando los agregauemos en el admin
    zone_position = models.FloatField(default=0.3)
    # ? 0.3 = 600
    zone_cost = models.FloatField(default=3000)

    # ? 3000 pesos

    def __str__(self):
        return str(self.zone_id)


class destinyPerson(models.Model):
    destiny_name = models.CharField('Nombre completo',max_length=200)
    destiny_id = models.CharField('ID',max_length=10, primary_key=True)
    destiny_phone = models.IntegerField('Telefono',blank=True)
    destiny_city = models.CharField('Ciudad',max_length=100, blank=True, null=True)
    destiny_adress = models.CharField('Direccion',max_length=100)
    destiny_neigth = models.ForeignKey(neighborhood, on_delete = models.CASCADE,help_text='Escoja su barrio')
    destity_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, help_text=' Final de Ctg -1- España -2- Ternera -3- inicio de Ctg')

    def __str__(self):
        return self.destiny_id


class logperson(models.Model):
    origin_id = models.CharField(max_length=10, primary_key=True)
    origin_nickname = models.CharField(max_length=20)
    origin_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.origin_id


class originPerson(models.Model):
    origin_name = models.CharField('Nombre completo' ,max_length=200)
    origin_id = models.CharField('Confirme su ID', max_length=10, primary_key=True)
    origin_ids = models.ForeignKey(logperson, on_delete=models.CASCADE)
    origin_phone = models.IntegerField('Telefono',blank=True)
    origin_city = models.CharField('Ciudad',max_length=100, blank=True, null=True)
    origin_address = models.CharField('Direccion',max_length=100)
    origin_neigth = models.ForeignKey(neighborhood, on_delete = models.CASCADE,help_text='Escoja su barrio')
    origin_zone = models.ForeignKey(Zone, on_delete=models.CASCADE, help_text=' Final de Ctg -1- España -2- Ternera -3- inicio de Ctg')

    def __str__(self):
        return self.origin_id


class Package(models.Model):
    status = [
        ('Bodega', 'En preparacion'),
        ('Ruta', 'En camino'),
        ('Recibido', 'Paquete enviado'),
        ('Error', 'Problemas en el envio')
    ]
    pack_id = models.AutoField(primary_key=True)
    pack_name = models.CharField('Paquete', max_length=100)
    pack_weight = models.FloatField('Peso')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    origin = models.ForeignKey(originPerson, on_delete=models.CASCADE)
    destiny = models.CharField('Destinatario',max_length=10, blank=True, default='ID')
    date_send = models.DateTimeField('Fecha de envio',blank=True, null=True)
    date_recibe = models.DateTimeField('Fecha de llegada estimada', blank=True, null=True)
    pack_status = models.CharField(max_length=10, choices=status, default='Bodega')
    pack_received = models.CharField(max_length=300, blank=True, default='Ninguno', null=True)
    cost = models.CharField(default=0, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.pack_id)
