from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets


def mainpage(request, *args, **kwargs):
    print(dir(request))
    if request.user.is_anonymous:
        return login(request, *args, **kwargs)
    else:
        return render(request, 'index.html', {})


def profile(request, *args, **kwargs):
    return render(request, 'profile.html', {})


def login(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
    return render(request, 'login.html', {})


def register(request, *args, **kwargs):
    return render(request, 'register.html')


class doctorView(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer


class patientView(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = patientSerializer

