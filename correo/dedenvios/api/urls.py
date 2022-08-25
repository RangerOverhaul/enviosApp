from django.urls import path
from dedenvios.api.api import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #Token 
    path('token/',  jwt_views.TokenObtainPairView.as_view(), name='tokenobtain'),
    path('token/refresh',  jwt_views.TokenRefreshView.as_view(), name='tokenrefresh'),
    # Users
    path('user/update/<str:pk>/', UpdateUser.as_view(), name='updateuser'),
    path('user/<str:pk>/', UserViewset.as_view({'get': 'retrieve'}), name='user'),
    path('user/', UserViewset.as_view({'get': 'list'}), name='userlist'),
    # REMITENTE - PERSON
    path('origin/<str:pk>/', PersonViewset.as_view({'get': 'retrieve'}), name='person'),
    path('origin/', PersonViewset.as_view({'get': 'list'}), name='personlist'),
    path('origin/delete/<str:pk>/', DeletePerson.as_view(), name='deleteperson'),
    path('origin/update/<str:pk>/', UpdatePerson.as_view(), name='updateperson'),
    # PAQUETE - PACK
    path('pack/', PackViewset.as_view({'get': 'list'}), name='packlist'),
    path('pack/<str:pk>/', PackViewset.as_view({'get': 'retrieve'}), name='pack'),
    path('pack/delete/<str:pk>/', DeletePack.as_view(), name='deletepack'),
    path('pack/update/<str:pk>/', UpdatePack.as_view(), name='updatepack'),
    # DESTINO - DESTINY
    path('destiny/', DestinyViewset.as_view({'get': 'list'}), name='destinylist'),
    path('destiny/<str:pk>/', DestinyViewset.as_view({'get': 'retrieve'}), name='destiny'),
    path('destiny/delete/<str:pk>/', DeleteDestiny.as_view(), name='deletedestiny'),
    path('destiny/update/<str:pk>/', UpdateDestiny.as_view(), name='updatepack'),
    # BARRIOS - NEIGTHBORHOOD
    path('neigth/', NeigthborViewset.as_view({'get': 'list'}), name='neihborslist'),
    path('neigth/delete/<str:pk>/', DeleteNeigh.as_view(), name='deletedestiny'),
    path('neigth/update/<str:pk>/', UpdateNeigh.as_view(), name='updateneigh'),
    path('neigth/<str:neigh_id>/', NeigthborViewset.as_view({'get': 'retrieve'}), name='destiny'),
    # ZONAS - ZONES
    path('zones/<int:zone_id>/', ZonesViewset.as_view({'get': 'retrieve'}), name='zones'),
    path('zones/delete/<int:pk>/', DeleteZone.as_view(), name='deletezone'),
    path('zones/update/<int:pk>/', UpdateNeigh.as_view(), name='updatezone'),
    path('zones/', ZonesViewset.as_view({'get': 'list'}), name='zoneslist'),

]
