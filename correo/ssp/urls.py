from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

#app_name = 'ssp'
urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='index'),
    path('log_out/', LogoutView.as_view(template_name='log_out.html'), name='log_out'),
    path('signup/', register, name='signup'),
    path('person/', create_person, name='create_person'),
    path('zone/', create_zone, name='create_zone'),
    path('neighbor/', create_neighbor, name='create_neighbor'),
    path('service/', create_service, name='create_service'),
    path('courier/', create_courier, name='create_courier'),
    path('sending/', create_packagesending, name='create_sending'),
]