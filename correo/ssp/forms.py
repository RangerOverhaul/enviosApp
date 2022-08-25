from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *


class PersonForm(forms.ModelForm):

    neighbor_person=forms.ModelChoiceField(
        queryset=neighborhood.objects.all()
    )

    class Meta:
        model = Person
        fields = ('name_person', 'identification_name', 'phone_person', 'type_person','neighbor_person')



class NeighborForm(forms.ModelForm):

    zone_neighbor=forms.ModelChoiceField(
        queryset=Zone.objects.all()
    )

    class Meta:
        model = neighborhood
        fields = ('name_neighbor', 'zone_neighbor')

class ZoneForm(forms.ModelForm):


    class Meta:
        model = Zone
        fields = ('id_zone', 'name_zone', 'zone_position')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name_service', 'cost_service')




class CourierForm(forms.ModelForm):

    class Meta:
        model = Courier
        fields = ('name_courier','identification_courier','phone_courier','last_location','available_courier')




class PackageSendingForm(forms.ModelForm):



    sender_person = forms.ModelChoiceField(
        queryset=Person.objects.all()
    )

    receiver_person = forms.ModelChoiceField(
        queryset=Person.objects.all()
    )

    pickup_zone = forms.ModelChoiceField(
        queryset=Zone.objects.all()
    )

    delivery_zone = forms.ModelChoiceField(
        queryset=Zone.objects.all()
    )



    class Meta:
        model = PackageSending
        fields = ('sender_person', 'address_pickup', 'pickup_zone', 'receiver_person', 'address_delivery', 'delivery_zone', 'service', 'assigned_courier','cost_sending')



class UserRegisterForm(UserCreationForm):
    userid = forms.CharField(label='ID', max_length=10)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = {k: "" for k in fields}