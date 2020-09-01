# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BedicalBed(models.Model):
    bedno = models.CharField(max_length=10)
    roomid = models.CharField(max_length=10)
    level = models.CharField(max_length=2, blank=True, null=True)
    ward = models.CharField(max_length=2, blank=True, null=True)
    room = models.CharField(max_length=2, blank=True, null=True)
    bed = models.CharField(max_length=2, blank=True, null=True)
    roomtype = models.CharField(max_length=20, blank=True, null=True)
    bedid = models.UUIDField(primary_key=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    distancetonursestation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.bedno}'

    class Meta:
        managed = False
        db_table = 'bedical_bed'


class BedicalBedbooking(models.Model):
    bookingid = models.UUIDField(primary_key=True)
    patientid = models.ForeignKey('BedicalPatient', models.DO_NOTHING, db_column='patientid')
    diagnosisid = models.ForeignKey('BedicalDiagnosis', models.DO_NOTHING, db_column='diagnosisid')
    admissiondate = models.DateField()
    equipment = models.TextField(blank=True, null=True)  # This field type is a guess.
    roomtype = models.CharField(max_length=20, blank=True, null=True)
    bedid = models.ForeignKey(BedicalBed, models.DO_NOTHING, db_column='bedid', blank=True, null=True)
    doctorid = models.ForeignKey('BedicalDoctor', models.DO_NOTHING, db_column='doctorid', blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_bedbooking'


class BedicalBedmanagement(models.Model):
    managementid = models.UUIDField(primary_key=True)
    patientid = models.ForeignKey('BedicalPatient', models.DO_NOTHING, db_column='patientid')
    admissiondate = models.DateField()
    dischargedate = models.DateTimeField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)  # This field type is a guess.
    bedstatus = models.CharField(max_length=50, blank=True, null=True)
    cleanbed = models.DateTimeField(blank=True, null=True)
    bedid = models.ForeignKey(BedicalBed, models.DO_NOTHING, db_column='bedid')
    diagnosisid = models.ForeignKey('BedicalDiagnosis', models.DO_NOTHING, db_column='diagnosisid', blank=True, null=True)
    doctorid = models.ForeignKey('BedicalDoctor', models.DO_NOTHING, db_column='doctorid', blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_bedmanagement'


class BedicalDiagnosis(models.Model):
    diagnosisid = models.UUIDField(primary_key=True)
    patientid = models.ForeignKey('BedicalPatient', models.DO_NOTHING, db_column='patientid')
    doctorid = models.ForeignKey('BedicalDoctor', models.DO_NOTHING, db_column='doctorid')
    icd10cmcode = models.CharField(max_length=255, blank=True, null=True)
    symptoms = models.CharField(max_length=100, blank=True, null=True)
    severity = models.CharField(max_length=10, blank=True, null=True)
    treatment = models.CharField(max_length=100, blank=True, null=True)
    medicine = models.CharField(max_length=100, blank=True, null=True)
    equipment = models.CharField(max_length=100, blank=True, null=True)
    surgery = models.BooleanField(blank=True, null=True)
    operationroom = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    diagnosisdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.icd10cmcode}'

    class Meta:
        managed = False
        db_table = 'bedical_diagnosis'


class BedicalDiagnosisEquipment(models.Model):
    equipmentid = models.UUIDField(primary_key=True)
    diganosisid = models.ForeignKey(BedicalDiagnosis, models.DO_NOTHING, db_column='diganosisid', blank=True, null=True)
    equipment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_diagnosis_equipment'


class BedicalDiagnosisMedicine(models.Model):
    medicineid = models.UUIDField(primary_key=True)
    diagnosisid = models.ForeignKey(BedicalDiagnosis, models.DO_NOTHING, db_column='diagnosisid', blank=True, null=True)
    medicine = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_diagnosis_medicine'


class BedicalDiagnosisSymptom(models.Model):
    symptomid = models.UUIDField(primary_key=True)
    diagnosisid = models.ForeignKey(BedicalDiagnosis, models.DO_NOTHING, db_column='diagnosisid', blank=True, null=True)
    symptom = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_diagnosis_symptom'


class BedicalDiagnosisTreatment(models.Model):
    treatmentid = models.UUIDField(primary_key=True)
    diagnosisid = models.ForeignKey(BedicalDiagnosis, models.DO_NOTHING, db_column='diagnosisid', blank=True, null=True)
    treatment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_diagnosis_treatment'


class BedicalDoctor(models.Model):
    doctorid = models.UUIDField(primary_key=True)
    doctorfirstname = models.CharField(max_length=150)
    doctorlastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1)
    contact = models.CharField(max_length=128)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.doctorlastname}, {self.doctorfirstname}'

    class Meta:
        managed = False
        db_table = 'bedical_doctor'


class BedicalNurse(models.Model):
    nurseid = models.UUIDField(primary_key=True)
    nursefirstname = models.CharField(max_length=150)
    nurselastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1)
    contact = models.CharField(max_length=128)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nurselastname}, {self.nursefirstname}'

    class Meta:
        managed = False
        db_table = 'bedical_nurse'


class BedicalOperationbooking(models.Model):
    operationbookingid = models.UUIDField(primary_key=True)
    patientid = models.ForeignKey('BedicalPatient', models.DO_NOTHING, db_column='patientid')
    diagnosisid = models.ForeignKey(BedicalDiagnosis, models.DO_NOTHING, db_column='diagnosisid')
    operationdate = models.DateField()
    doctorid = models.ForeignKey(BedicalDoctor, models.DO_NOTHING, db_column='doctorid')
    operationroom = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bedical_operationbooking'


class BedicalPatient(models.Model):
    patientid = models.UUIDField(primary_key=True)
    patientfirstname = models.CharField(max_length=150)
    patientlastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    contact = models.CharField(max_length=128)
    location = models.CharField(max_length=255)
    emergencycontact = models.CharField(max_length=128)
    bloodgroup = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f'{self.patientlastname}, {self.patientfirstname}'

    class Meta:
        managed = False
        db_table = 'bedical_patient'


class BedicalPayment(models.Model):
    patientid = models.ForeignKey(BedicalPatient, models.DO_NOTHING, db_column='patientid')
    insurancecover = models.BooleanField(blank=True, null=True)
    paymentamount = models.TextField(blank=True, null=True)  # This field type is a guess.
    paymentstatus = models.CharField(max_length=50, blank=True, null=True)
    doctorapproval = models.DateTimeField(blank=True, null=True)
    financialclear = models.DateTimeField(blank=True, null=True)
    insurer = models.CharField(max_length=100, blank=True, null=True)
    admissiondate = models.DateField(blank=True, null=True)
    dischargedate = models.DateTimeField(blank=True, null=True)
    paymentid = models.UUIDField(primary_key=True)
    bedid = models.ForeignKey(BedicalBed, models.DO_NOTHING, db_column='bedid')
    startdischarge = models.DateTimeField(blank=True, null=True)
    managementid = models.ForeignKey(BedicalBedmanagement, models.DO_NOTHING, db_column='managementid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bedical_payment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
