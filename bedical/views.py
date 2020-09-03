import datetime, uuid
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .serializers import *
from .models import *
from .filters import *
from dal import autocomplete
from .forms import *
from rest_framework import viewsets, filters
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django_filters.views import FilterView


class BedBMAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return BedicalBedmanagement.objects.none()
        qs = BedicalBedmanagement.objects.all()

        if self.q:
            qs = qs.filter(patientid_id__patientfirstname__istartswith=self.q)

        return qs


@login_required(login_url='/login/')
def mainpage(request, *args, **kwargs):
    return redirect('profile')

@login_required(login_url='/login/')
def searchpage(request, *args, **kwargs):
    return render(request, 'search.html')

@login_required(login_url='/login/')
def patientprofile(request, bid, *args, **kwargs):

    context = {
        'bid': bid,
    }
    return render(request, 'patient.html', context)

@login_required(login_url='/login/')
def staffprofile(request, bid, *args, **kwargs):
    context = {
        'bid': bid,
    }
    return render(request, 'staff.html', context)


@login_required(login_url='/login/')
def admissionpage(request, *args, **kwargs):
    form = BedManageForm()
    if request.method == 'POST':
        form = BedBookingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()

    bbm = BedmanagementFilter(request.GET, queryset=BedicalBedmanagement.objects.order_by('-admissiondate').all())
    page = request.GET.get('page', 1)
    paginator = Paginator(bbm.qs, 10)
    try:
        bbms = paginator.page(page)
    except PageNotAnInteger:
        bbms = paginator.page(1)
    except EmptyPage:
        bbms = paginator.page(paginator.num_pages)
    context = {
        'filterbm': bbm,
        'bedmanage': bbms,
        'form': form,
    }
    return render(request, 'bedmanagement.html', context)

@login_required(login_url='/login/')
def appointmentpage(request, *args, **kwargs):
    form = BedBookingForm()
    if request.method == 'POST':
        form = BedBookingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()

    bb = BedbookingFilter(request.GET, queryset=BedicalBedbooking.objects.order_by('-admissiondate').all())
    page = request.GET.get('page', 1)
    paginator = Paginator(bb.qs, 10)
    try:
        bbs = paginator.page(page)
    except PageNotAnInteger:
        bbs = paginator.page(1)
    except EmptyPage:
        bbs = paginator.page(paginator.num_pages)
    context = {
        'filterbs': bb,
        'bedbook': bbs,
        'form': form,
    }
    return render(request, 'bedbooking.html', context)

@login_required(login_url='/login/')
def patientpage(request, *args, **kwargs):
    return render(request, 'patients.html', {})

@login_required(login_url='/login/')
def dischargepage(request, *args, **kwargs):
    bbm = BedmanagementFilter(request.GET, queryset=BedicalBedmanagement.objects.order_by('-admissiondate').all())
    page = request.GET.get('page', 1)
    paginator = Paginator(bbm.qs, 10)
    try:
        bbms = paginator.page(page)
    except PageNotAnInteger:
        bbms = paginator.page(1)
    except EmptyPage:
        bbms = paginator.page(paginator.num_pages)
    context = {
        'filterbm': bbm,
        'bedmanage': bbms,
    }
    return render(request, 'discharge.html', context)

@login_required(login_url='/login/')
def dashboardpage(request, *args, **kwargs):
    context = {
        'tpd': msql(rawsqlstr['Total Patient Discharged']).to_numpy().ravel().item(),
        'tpa': msql(rawsqlstr['Total Patient Admitted']).to_numpy().ravel().item(),
        'ab': msql(rawsqlstr['Available Beds']).to_numpy().ravel().item(),
        'pie': msql(rawsqlstr['Patient in Emergency']).to_numpy().ravel().item(),
    }

    return render(request, 'dash.html', context)


@login_required(login_url='/login/')
def profilepage(request, *args, **kwargs):
    context = None
    getgroup = list(request.user.groups.values_list('name', flat=True))
    if 'Nurse' in getgroup:
        bn = BedicalNurse.objects.select_related().filter(nursefirstname=request.user.first_name, nurselastname=request.user.last_name)[0]
        bmdata = BedicalBedmanagement.objects.filter(department=bn.department, bedstatus='Occupied')
        context = {
            'admission_list': bmdata,
            'bio': {'lastname': bn.nurselastname, 'firstname': bn.nursefirstname, 'contact': bn.contact, 'department': bn.department, 'gender': bn.gender},
        }
    elif 'Doctor' in getgroup:
        bd = BedicalDoctor.objects.select_related().filter(doctorfirstname=request.user.first_name, doctorlastname=request.user.last_name)[0]
        bmdata = BedicalBedmanagement.objects.filter(doctorid=bd.doctorid, bedstatus='Occupied')
        context = {
            'admission_list': bmdata,
            'bio': {'lastname': bd.doctorlastname, 'firstname': bd.doctorfirstname, 'contact': bd.contact,
                    'department': bd.department, 'gender': bd.gender},
        }
    return render(request, 'profile.html', context)


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
        data = {'charts': {}}
        for i, (key, val) in enumerate(rawsqlstr.items()):
            data['charts'][key] = msql(val).to_dict('list')
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


class patientSearchiew(ObjectMultipleModelAPIView):
    def get_querylist(self):
        idstr = self.request.query_params['id']
        idobj = uuid.UUID(idstr)
        querylist = (
            {
                'queryset': BedicalBedbooking.objects.filter(patientid=idobj),
                'serializer_class': bedbookingSerializer,
                'label': 'bedbooking'
            },
            {
                'queryset': BedicalBedmanagement.objects.filter(patientid=idobj),
                'serializer_class': bedmanagementSerializer,
                'label': 'bedmanagement'
            },
            {
                'queryset': BedicalDiagnosis.objects.filter(patientid=idobj),
                'serializer_class': diagnosisSerializer,
                'label': 'diagnosis'
            },
            # {
            #     'queryset': BedicalDoctor.objects.all(),
            #     'serializer_class': doctorSerializer,
            #     'label': 'doctor'
            # },
            {
                'queryset': BedicalOperationbooking.objects.filter(patientid=idobj),
                'serializer_class': operationbookingSerializer,
                'label': 'operationbooking'
            },
            {
                'queryset': BedicalPatient.objects.filter(patientid=idobj),
                'serializer_class': patientSerializer,
                'label': 'patient'
            },
            {
                'queryset': BedicalPayment.objects.filter(patientid=idobj),
                'serializer_class': paymentSerializer,
                'label': 'payment'
            },
        )
        return querylist


class doctorSearchiew(ObjectMultipleModelAPIView):
    def get_querylist(self):
        idstr = self.request.query_params['id']
        idobj = uuid.UUID(idstr)
        querylist = (
            {
                'queryset': BedicalBedbooking.objects.filter(doctorid=idobj),
                'serializer_class': bedbookingSerializer,
                'label': 'bedbooking'
            },
            {
                'queryset': BedicalBedmanagement.objects.filter(doctorid=idobj),
                'serializer_class': bedmanagementSerializer,
                'label': 'bedmanagement'
            },
            {
                'queryset': BedicalDiagnosis.objects.filter(doctorid=idobj),
                'serializer_class': diagnosisSerializer,
                'label': 'diagnosis'
            },
            {
                'queryset': BedicalDoctor.objects.filter(doctorid=idobj),
                'serializer_class': doctorSerializer,
                'label': 'doctor'
            },
            {
                'queryset': BedicalOperationbooking.objects.filter(doctorid=idobj),
                'serializer_class': operationbookingSerializer,
                'label': 'operationbooking'
            },
            # {
            #     'queryset': BedicalPatient.objects.filter(patientid=idobj),
            #     'serializer_class': patientSerializer,
            #     'label': 'patient'
            # },
            {
                'queryset': BedicalPayment.objects.filter(patientid=idobj),
                'serializer_class': paymentSerializer,
                'label': 'payment'
            },
        )
        return querylist


'''class patientSearchiew(ObjectMultipleModelAPIView):
    querylist = (
        {
            'queryset': BedicalBed.objects.all(),
            'serializer_class': bedSerializer,
            'label': 'bed',
        },
        {
            'queryset': BedicalBedbooking.objects.all(),
            'serializer_class': bedbookingSerializer,
            'label': 'bedbooking'
        },
        {
            'queryset': BedicalBedmanagement.objects.all(),
            'serializer_class': bedmanagementSerializer,
            'label': 'bedmanagement'
        },
        {
            'queryset': BedicalDiagnosis.objects.all(),
            'serializer_class': diagnosisSerializer,
            'label': 'diagnosis'
        },
        {
            'queryset': BedicalDoctor.objects.all(),
            'serializer_class': doctorSerializer,
            'label': 'doctor'
        },
        {
            'queryset': BedicalOperationbooking.objects.all(),
            'serializer_class': operationbookingSerializer,
            'label': 'operationbooking'
        },
        {
            'queryset': BedicalPatient.objects.all(),
            'serializer_class': patientSerializer,
            'label': 'patient'
        },
        {
            'queryset': BedicalPayment.objects.all(),
            'serializer_class': paymentSerializer,
            'label': 'payment'
        },
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('patientid',)
    '''