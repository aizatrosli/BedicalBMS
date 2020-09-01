from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from dal import autocomplete
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class BedBookingForm(ModelForm):
    class Meta:
        model = BedicalBedbooking
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'roomtype', 'bedid', 'doctorid', 'department']


class BedManageForm(ModelForm):
    patientid_ = forms.ModelChoiceField(
        queryset=BedicalBedmanagement.objects.all(),
        widget=autocomplete.ModelSelect2(url='bm-autocomplete')
    )

    class Meta:
        model = BedicalBedmanagement
        fields = ['patientid', 'diagnosisid', 'admissiondate', 'bedstatus', 'bedid', 'doctorid', 'department']
