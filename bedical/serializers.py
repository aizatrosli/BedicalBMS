from .models import patient,doctor
from rest_framework import serializers


class patientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient
        fields = (
            "patientid",
            "patientfirstname",
            "patientlastname",
            "gender",
            "dob",
            "contact",
            "location",
            "emergencycontact",
        )


class doctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = doctor
        fields = (
            "doctorid",
            "doctorfirstname",
            "doctorlastname",
            "gender",
            "contact",
            "department",
        )
