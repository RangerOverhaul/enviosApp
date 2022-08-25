from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from dedenvios.models import *
from rest_framework_simplejwt import *
from rest_framework.permissions import IsAuthenticated
from jwt import *
from .serializers import *

 # Autenticaded User for login
class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    queryset = logperson.objects.all()
    serializer_class = Usererializer
    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, origin_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nuevo usuario creado'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUser(UpdateAPIView):
    permission_classes = (IsAuthenticated)
    serializer_class = Usererializer
    queryset = logperson.objects.all()
    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, origin_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)



# PERSONS REMITENTE

class PersonViewset(viewsets.ModelViewSet):
    queryset = originPerson.objects.all()
    serializer_class = Personserializer
    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, origin_ids=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nuevo remitente creado'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePerson(DestroyAPIView):
    queryset = originPerson.objects.all()
    serializer_class = Personserializer

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, origin_ids=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    # eliminacion logica:

    """def delete(self, request, pk=None):
        person = self.get_queryset().filter(origin_ids=pk).first()
        if person:
            person.state = False
            person.save()
            return Response({'message': 'Remitente eliminado'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Remitente no encontrado'}, status=status.HTTP_400_BAD_REQUEST)"""

class UpdatePerson(UpdateAPIView):
    serializer_class = Personserializer
    queryset = originPerson.objects.all()

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, origin_ids=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'Remitente no encontrado'}, status=status.HTTP_400_BAD_REQUEST)



# ZONES

class ZonesViewset(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = Zoneserializer

    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, zone_id= kwargs.get('zone_id'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nueva zona creada'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteZone(DestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = Zoneserializer

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, zone_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)


class UpdateZone(UpdateAPIView):
    serializer_class = Zoneserializer
    queryset = Zone.objects.all()

    def patch(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, zone_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'zona no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
# PAQUETES - PACKS

class PackViewset(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = Packserializer

    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, pack_id= kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nuevo remitente creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePack(DestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = Packserializer

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, pack_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)


class UpdatePack(UpdateAPIView):
    serializer_class = Packserializer
    queryset = Package.objects.all()

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, pack_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'Paquete no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

# DESTINO  DESTINY

class DestinyViewset(viewsets.ModelViewSet):
    queryset = destinyPerson.objects.all()
    serializer_class = Destinyserializer

    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, destiny_id= kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nuevo destinatario creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteDestiny(DestroyAPIView):
    queryset = destinyPerson.objects.all()
    serializer_class = Destinyserializer

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, destiny_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

class UpdateDestiny(UpdateAPIView):
    serializer_class = Destinyserializer
    queryset = destinyPerson.objects.all()

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, destiny_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'Destinatario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

# BARRIOS NEIGTHBORHOOD

class NeigthborViewset(viewsets.ModelViewSet):
    queryset = neighborhood.objects.all()
    serializer_class = Neihborserializer

    def retrieve(self, request, *args, **kwargs):
        query =get_object_or_404(self.queryset, neigh_id= kwargs.get('neigh_id'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Nuevo barrio creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteNeigh(DestroyAPIView):
    queryset = neighborhood.objects.all()
    serializer_class = Neihborserializer

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, neigh_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        return Response(serializer.data)

class UpdateNeigh(UpdateAPIView):
    serializer_class = Neihborserializer
    queryset = neighborhood.objects.all()

    def get(self, request, *args, **kwargs):
        query = get_object_or_404(self.queryset, neigh_id=kwargs.get('pk'))
        serializer = self.serializer_class(query)
        if serializer:
            return Response(serializer.data)
        return Response({'message': 'Barrio no encontrado'}, status=status.HTTP_400_BAD_REQUEST)