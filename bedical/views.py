from django.shortcuts import render, redirect
from .serializers import *
from .models import *
from .forms import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate, login, logout


def mainpage(request, *args, **kwargs):
    context = {
        'titlec1': 'Total Patients',
        'titlec2': 'Clearance Time by Insurance Company',
        'titlec3': 'Outpatient to Inpatient Conversion',
        'titlec4': 'Cases by Insurance Company',
        'titlec5': 'Cases by Division',
        'titlec6': 'Bed Vacancy by date',
    }
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'home.html', context)


def registrationpage(request, *args, **kwargs):
    return render(request, 'registration.html', {})


def patientpage(request, *args, **kwargs):
    return render(request, 'patient.html', {})


def staffpage(request, *args, **kwargs):
    return render(request, 'staff.html', {})


def dashboardpage(request, *args, **kwargs):
    return render(request, 'dash.html', {})


def appointmentpage(request, *args, **kwargs):
    return render(request, 'appointment.html', {})


def profilepage(request, *args, **kwargs):
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


def registerpage(request, *args, **kwargs):
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


class DashboardData(APIView):
    authentication_classes = []#[authentication.TokenAuthentication]
    permission_classes = []#[permissions.IsAdminUser]

    def get(self, request, format=None):
        data = {
            'TotalMalePatient' : 100,
            'TotalFemalePatient' : 200,
        }
        return Response(data)


class bedView(viewsets.ModelViewSet):
    queryset = BedicalBed.objects.all()
    serializer_class = bedSerializer


class bedbookingView(viewsets.ModelViewSet):
    queryset = BedicalBedbooking.objects.all()
    serializer_class = bedbookingSerializer


class bedmanagementView(viewsets.ModelViewSet):
    queryset = BedicalBedmanagement.objects.all()
    serializer_class = bedmanagementSerializer


class diagnosisView(viewsets.ModelViewSet):
    queryset = BedicalDiagnosis.objects.all()
    serializer_class = diagnosisSerializer


class doctorView(viewsets.ModelViewSet):
    queryset = BedicalDoctor.objects.all()
    serializer_class = doctorSerializer


class operationbookingView(viewsets.ModelViewSet):
    queryset = BedicalOperationbooking.objects.all()
    serializer_class = operationbookingSerializer


class patientView(viewsets.ModelViewSet):
    queryset = BedicalPatient.objects.all()
    serializer_class = patientSerializer


class paymentView(viewsets.ModelViewSet):
    queryset = BedicalPayment.objects.all()
    serializer_class = paymentSerializer

