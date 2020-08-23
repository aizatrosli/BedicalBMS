from django.shortcuts import render, redirect
from .serializers import *
from .models import *
from .forms import *
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout


def mainpage(request, *args, **kwargs):
    print(dir(request))
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html', {})


def profile(request, *args, **kwargs):
    return render(request, 'profile.html', {})


def loginpage(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if 'login' in request.POST and user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {})


def register(request, *args, **kwargs):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


class doctorView(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = doctorSerializer


class patientView(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = patientSerializer

