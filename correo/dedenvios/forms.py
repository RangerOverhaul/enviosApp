from django import forms
from django.forms import inlineformset_factory, ModelForm, BaseModelFormSet, BaseInlineFormSet
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class Datap(forms.ModelForm):
    class Meta:
        model = originPerson
        fields = ['origin_phone', 'origin_city', 'origin_address']

class UserRegisterForm(UserCreationForm):
    userid = forms.CharField(label='ID',max_length=10)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class sendPack(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ['date_recibe', 'pack_status', 'pack_received ', 'cost', 'destiny', 'origin']


class sendDestiny(forms.ModelForm):
    class Meta:
        model = destinyPerson
        fields = '__all__'


class dataUser(forms.ModelForm):
    class Meta:
        model = originPerson
        fields = '__all__'
