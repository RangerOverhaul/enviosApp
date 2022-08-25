from django.shortcuts import render
from .models import Person,neighborhood
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def create_neighbor(request):
    title = 'Create neighborhood'

    if request.method == 'POST':
        form = NeighborForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NeighborForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createneighbor.html', context)



def create_zone(request):
    title = 'Create Zone'

    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ZoneForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createzone.html', context)


def create_person(request):
    title = 'Create Person'

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createperson.html', context)



def create_courier(request):
    title = 'Create Courier'

    if request.method == 'POST':
        form = CourierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourierForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createcourier.html', context)




def create_service(request):
    title = 'Create Service'

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ServiceForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createservice.html', context)


def create_packagesending(request):
    title = 'Create Service Sending Package'

    if request.method == 'POST':
        form = PackageSendingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PackageSendingForm()

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'ssp/createsending.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data['username']
            messages.success(request, f'Usuario {nickname} ha sido creado.')
            return redirect('index')

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

