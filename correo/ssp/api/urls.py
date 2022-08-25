from django.urls import path
from ssp.api.api import person_api_view, person_detail_view, courier_api_view,zone_api_view,service_api_view,neighborhood_api_view

urlpatterns =[
    path('persons/', person_api_view,name='person_api_view'),
     path('persons/<str:ident>', person_detail_view,name='person_detail_api_view'),
    path('couriers/', courier_api_view,name='courier_api_view'),
    path('zones/', zone_api_view,name='zone_api_view'),
    path('services/', service_api_view,name='service_api_view'),
    path('neighborhoods/', neighborhood_api_view,name='neighbor_api_view'),

]

