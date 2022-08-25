from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ssp.api.serializers import PersonSerializer,CourierSerializer,ZoneSerializer,ServiceSerializer,neighborhoodSerializer
from ssp.models import Person,Courier,Zone,Service,neighborhood,PackageSending

@api_view(['GET','POST'])
def person_api_view(request):

    if request.method == 'GET':
        persons = Person.objects.all()
        person_serializer = PersonSerializer(persons,many=True)
        return Response(person_serializer.data)


    if request.method == 'POST':
        
        person_serializer = PersonSerializer(data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return Response(person_serializer.data)
        return Response(person_serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def person_detail_view(request,ident):
    identification = Person.objects.filter(identification_name=ident)

    if identification.exists():
        identification = identification.latest('identification_name')

        if request.method == 'GET':
            person_serializer = PersonSerializer(identification)
            return Response(person_serializer.data, status=status.HTTP_200_OK)

        if request.method == 'PUT':
            person_serializer = PersonSerializer(identification, data=request.data)
            if person_serializer.is_valid():
                person_serializer.save()
                return Response({'message': 'Person was updated.'}, status=status.HTTP_200_OK)
            return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            identification.delete()
            return Response({'message': 'Person was deleted.'}, status=status.HTTP_200_OK)

    return Response({'message': 'Person does not exist.'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','POST'])
def courier_api_view(request):

    if request.method == 'GET':
        courier = Courier.objects.all()
        courier_serializer = CourierSerializer(courier,many=True)
        return Response(courier_serializer.data)
     
    
    if request.method == 'POST':
        
        courier_serializer = CourierSerializer(data=request.data)
        if courier_serializer.is_valid():
            courier_serializer.save()
            return Response(courier_serializer.data)
        return Response(courier_serializer.errors)                 





@api_view(['GET','POST'])
def zone_api_view(request):

    if request.method == 'GET':
        zone = Zone.objects.all()
        zone_serializer = ZoneSerializer(zone,many=True)
        return Response(zone_serializer.data)     


    if request.method == 'POST':
        
        zone_serializer = ZoneSerializer(data=request.data)
        if zone_serializer.is_valid():
            zone_serializer.save()
            return Response(zone_serializer.data)
        return Response(zone_serializer.errors)       



@api_view(['GET','POST'])
def service_api_view(request):

    if request.method == 'GET':
        service = Service.objects.all()
        service_serializer = ServiceSerializer(service,many=True)
        return Response(service_serializer.data)

@api_view(['GET','POST'])
def neighborhood_api_view(request):

    if request.method == 'GET':
        neighbor = neighborhood.objects.all()
        neighbor_serializer = neighborhoodSerializer(neighbor,many=True)
        return Response(neighbor_serializer.data)


    if request.method == 'POST':
        
        neighbor_serializer = neighborhoodSerializer(data=request.data)
        if neighbor_serializer.is_valid():
            neighbor_serializer.save()
            return Response(neighbor_serializer.data)
        return Response(neighbor_serializer.errors)      
