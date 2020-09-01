from django_filters import *
from .models import *


class BedmanagementFilter(FilterSet):

    class Meta:
        model = BedicalBedmanagement
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'bedstatus', 'bedid', 'doctorid', 'department']


class BedbookingFilter(FilterSet):

    class Meta:
        model = BedicalBedbooking
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'roomtype', 'bedid', 'doctorid', 'department']

