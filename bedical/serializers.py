from .models import *
from rest_framework import serializers


class bedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalBed
        fields = (
            "__all__"
        )


class bedbookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalBedbooking
        fields = (
            "__all__"
        )


class bedmanagementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalBedmanagement
        fields = (
            "__all__"
        )


class diagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalDiagnosis
        fields = (
            "__all__"
        )


class doctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalDoctor
        fields = (
            "__all__"
        )


class operationbookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalOperationbooking
        fields = (
            "__all__"
        )


class patientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalPatient
        fields = (
            "__all__"
        )


class paymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedicalPayment
        fields = (
            "__all__"
        )
