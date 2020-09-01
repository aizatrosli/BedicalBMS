from django_filters import *
from .models import *
from .rawsql import *
from django.db import connection
import pandas as pd
from collections import OrderedDict

rawsqlstr = OrderedDict({
    'Inpatient & Outpatient': raw_a,
    'Inpatient & Outpatient by Month': raw_b,
    'Average Length of Stay': raw_c,
    'Bed Availibility': raw_d,
    'Total Patient Discharged': raw_e,
    'Total Patient Admitted': raw_f,
    'Available Beds': raw_g,
    'Patient in Emergency': raw_h,
    'Number of Patient per Doctor': raw_i,
    'Number of Admission by Doctor': raw_j,
    })


def msql(strdata):
    cursor = connection.cursor()
    cursor.execute(strdata)
    row = cursor.fetchall()
    column = [x[0] for x in cursor.description]
    cursor.close()
    return pd.DataFrame(row, columns=column)


class BedmanagementFilter(FilterSet):

    class Meta:
        model = BedicalBedmanagement
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'bedstatus', 'bedid', 'doctorid', 'department']


class BedbookingFilter(FilterSet):

    class Meta:
        model = BedicalBedbooking
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'roomtype', 'bedid', 'doctorid', 'department']

