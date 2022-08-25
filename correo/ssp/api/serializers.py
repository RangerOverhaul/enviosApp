from rest_framework import serializers
from ssp.models import Person,Courier,Service,Zone,neighborhood,PackageSending



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name_person','identification_name', 'phone_person', 'type_person','neighbor_person')

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('name_courier','identification_courier', 'phone_courier', 'last_location','available_courier')



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id_service','name_service', 'cost_service')


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ('id_zone','name_zone', 'zone_position')



class neighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = neighborhood
        fields = ('name_neighbor','zone_neighbor')

        

    