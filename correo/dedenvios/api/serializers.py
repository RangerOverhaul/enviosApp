from rest_framework import  serializers
from dedenvios.models import *


class Packserializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields='__all__'

class Personserializer(serializers.ModelSerializer):
    class Meta:
        model = originPerson
        exclude= ['origin_id']


class Destinyserializer(serializers.ModelSerializer):
    class Meta:
        model = destinyPerson
        fields = '__all__'


class Neihborserializer(serializers.ModelSerializer):
    class Meta:
        model = neighborhood
        fields = '__all__'


class Zoneserializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class Usererializer(serializers.ModelSerializer):
    class Meta:
        model = logperson
        fields = '__all__'