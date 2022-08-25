import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import *
from django.template import loader
from .forms import Datap, UserRegisterForm, sendPack, sendDestiny, dataUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import timedelta

# Create your views here.
@login_required
def index(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    try:
        fin = logperson.objects.get(origin_nickname=current_user)
    except Exception as e:
        messages.success(request, f'Usuario {current_user} no ha sido creado.')

    iduser = fin.origin_id
    h = ' Bienvenido '
    context = {
        'h': h,
        'iduser': iduser,
        'current_user': current_user
    }
    return render(request, 'index.html', context)

@login_required
def userdata(request):
    tittle = ' Registro de datos '
    userformSet = inlineformset_factory(logperson, originPerson, exclude=('origin_ids',), max_num=1)

    if request.method == 'POST':
        #form = dataUser(request.POST)
        current_user = get_object_or_404(User, pk=request.user.pk)
        fino = logperson.objects.get(origin_nickname=current_user)
        fin = logperson.objects.get(pk=fino.origin_id)
        form = userformSet(request.POST, instance=fin)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = userformSet()
    context = {
        'tittle': tittle,
        'form': form
    }
    return render(request, 'userdata.html', context)


@login_required
def history(request):
    tittle = ' Historial de envios '
    current_user = get_object_or_404(User, pk=request.user.pk)
    fino = logperson.objects.get(origin_nickname=current_user)
    pac = Package.objects.filter(origin=fino.origin_id)
    context = {
        'tittle': tittle,
        'pac': pac,
    }
    return render(request, 'history.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['username']
            id = form.cleaned_data['userid']
            pas = form.cleaned_data['password1']
            logan = logperson(origin_id=id, origin_nickname=nickname, origin_pass=pas)
            logan.save()
            messages.success(request, f'Usuario {nickname} ha sido creado.')
            return redirect('loggin')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def register2(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['username']
            id = form.cleaned_data['userid']
            pas = form.cleaned_data['password1']
            logan = logperson(origin_id=id, origin_nickname=nickname, origin_pass=pas)
            logan.save()
            messages.success(request, f'Usuario {nickname} ha sido creado.')
            return redirect('loggin')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def user(request, origin, destiny):
    person = originPerson.objects.filter(origin_id=origin)
    persond = destinyPerson.objects.filter(destiny_id=destiny)
    if person.exists():
        person = person[0]
        persond = persond[0]
        exists = True
    else:
        person = ' Does not exist in DB'
        exists = False
    context = {
        'person': person,
        'persond': persond,
        'exists': exists
    }
    return render(request, 'dedenvios/datos.html', context)


def thing(request, userid):
    tittle = ' Datos de Recogida del Paquete'
    try:
        find = originPerson.objects.get(origin_id=userid)
    except Exception as e:
        messages.success(request, f'Usuario {userid} no ha registrado sus datos.')
        return redirect('userdata')

    if request.method == 'POST':
        form = Datap(request.POST)
        if form.is_valid():
            tel = form.cleaned_data.get('origin_phone')
            dir = form.cleaned_data.get('origin_city')
            ad = form.cleaned_data.get('origin_address')
            find.origin_phone = tel
            find.origin_city = dir
            find.origin_address = ad
            return redirect('datos')
    else:
        form = Datap()
    context = {
        'tittle': tittle,
        'form': form
    }

    return render(request, 'thing.html', context)

def datos(request):
    tittle = ' Datos del destinatario '
    if request.method == 'POST':
        form = sendDestiny(request.POST)
        if form.is_valid():
            current_user = get_object_or_404(User, pk=request.user.pk)
            fino = logperson.objects.get(origin_nickname=current_user)
            userid = fino.origin_id
            desid = form.cleaned_data.get('destiny_id')
            form.save()
            return redirect('package/' + userid +'/'+ desid)
    else:
        form = sendDestiny()
    context = {
        'tittle': tittle,
        'form': form
    }
    return render(request, 'datos.html', context)

def package(request, userid, destid):
    tittle = ' Datos del Paquete '
    userformSet = inlineformset_factory(originPerson, Package, exclude=('date_recibe','date_send' ,'pack_status', 'pack_received ', 'cost', 'destiny', 'origin',), max_num=1)

    if request.method == 'POST':
        # form = dataUser(request.POST)
        # datos del remitente
        fin = originPerson.objects.get(pk=userid)
        # datos del destinatario
        dst = destinyPerson.objects.get(destiny_id=destid)
        # guardando el form
        form = userformSet(request.POST, instance=fin)
        if form.is_valid():
            form.save()
            #return redirect('index')
        else:
            return redirect('./')
        # datos del paquete
        fn = Package.objects.get(pack_status='Bodega')
        # datos del servicio
        env = Service.objects.get(type_service=fn.service)
        # datos de zonas de remitente y destinatario
        dstzone = str(dst.destity_zone)
        orgzone = str(fin.origin_zone)
        # datos de tabla de zonas
        zo = Zone.objects.get(zone_id=dstzone)
        # mas datos de zonas de personas
        cstser = str(env.cost_service)
        zopos = str(zo.zone_position)
        cstzone = str(zo.zone_cost)
        # id del destino en paquete
        fn.destiny = destid
        # calculo de viaje entre zonas
        zoo = int(dstzone) - int(orgzone)
        print(zoo)
        if zoo == 0:
            zoo = 1
        # calculo del costo del envio
        cst = float(cstser) + ((abs(zoo) * float(cstzone)) + (float(zopos) * (abs(zoo) * float(cstzone))))
        fn.cost = cst
        fn.pack_status = 'Ruta'
        ahora = datetime.now()
        fn.date_send = ahora
        tisn = (ahora + timedelta(hours=22))
        fn.date_recibe = tisn
        fn.save()
        return redirect('history')
    else:
        form = userformSet()

    context = {
        'tittle': tittle,
        'form': form
    }
    return render(request, 'userdata.html', context)

