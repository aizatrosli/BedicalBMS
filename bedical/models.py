import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

genders = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Unknown'),
)
wards = (
    ('S', 'South'),
    ('N', 'North'),
    ('E', 'East'),
    ('W', 'West'),
)
roomtypes = (
    ('2 Bedded',),
    ('Single bedded',),
    ('4 Bedded',),
)

# Create your models here.

class patient(models.Model):

    patientid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patientfirstname = models.CharField(max_length=50)
    patientlastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=genders)
    dob = models.DateField()
    contact = PhoneNumberField()
    location = models.CharField(max_length=255)
    emergencycontact = PhoneNumberField()

    def __str__(self):
        return "{}:{},{}".format(self.patientid, self.patientlastname, self.patientfirstname)


class doctor(models.Model):

    doctorid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctorfirstname = models.CharField(max_length=50)
    doctorlastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=genders)
    contact = PhoneNumberField()
    department = models.CharField(max_length=255)

    def __str__(self):
        return "{}:{},{}".format(self.doctorid, self.doctorlastname, self.doctorfirstname)
'''

class diagnosis(models.Model):
    patientid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctorid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagnosiscode = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255)
    equipmentneeded = models.CharField(max_length=255)
    operationroom = models.CharField(max_length=255)

    def __str__(self):
        return self.patientid


class bedbooking(models.Model):
    bookingid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patientid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    admissiondate = models.DateField()
    equipmentid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    roomtype = models.CharField(max_length=50)
    bedid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.bookingid


class operationbooking(models.Model):
    bookingid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patientid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operationdate = models.DateField()
    operationroom = models.CharField(max_length=255)

    def __str__(self):
        return self.bookingid


class bed(models.Model):

    level = models.PositiveSmallIntegerField()
    ward = models.CharField(max_length=1, choices=wards)
    room = models.PositiveSmallIntegerField()
    roomtype = models.CharField(max_length=1, choices=roomtypes)
    bed = models.CharField(max_length=1)
    bedid = models.CharField(max_length=10, editable=False, unique=True, default="{}{}{}{}".format(level, ward, room, bed))

    def __str__(self):
        return self.bedid


class bedmanagement(models.Model):
    patientid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bedid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admissiondate = models.DateField()
    dischargedate = models.DateField()
    equipmentid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bedstatus = models.CharField(max_length=255)

    def __str__(self):
        return self.patientid


class equipment(models.Model):
    equipmentid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipmentdesc = models.CharField(max_length=255)

    def __str__(self):
        return equipment.id

'''