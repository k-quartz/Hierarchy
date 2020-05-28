from django.db import models
from django.utils import timezone


# Create your models here.
class Products(models.Model):
    IDProduct = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Provider = models.CharField(max_length=255)
    Category_it = models.CharField(max_length=255)
    Category_en = models.CharField(max_length=255)
    UnitQuantity_it = models.CharField(max_length=255)
    UnitPrice = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class BloodGroup(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    bloodgroupid = models.AutoField(primary_key=True)
    bloodgroup = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'bloodgroup'


class States(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    statesid = models.AutoField(primary_key=True)
    states = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'states'


class City(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    cityid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'city'


class OccupationType(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    occupationtypeid = models.AutoField(primary_key=True)
    occupationtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'occupationtype'


class ResidenceType(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    residencetypeid = models.AutoField(primary_key=True)
    residencetype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'residencetype'


class RelationType(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    relationtypeid = models.AutoField(primary_key=True)
    relationtype = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'relationtype'


class Member(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    memberid = models.AutoField(
        primary_key=True, editable=False)
    memberdate = models.DateTimeField(default=timezone.now)
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    mobile1 = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    mem_img = models.ImageField(upload_to='member_pics')
    dob = models.DateTimeField(default=timezone.now)

    def newlocation(self, filename):
        filspilt = filename.split(".")
        exten = filspilt[-1]
        return "newfile1"+"."+exten.lower()

    class Meta:
        managed = False
        db_table = 'member'


class MemberPrt(models.Model):
    memberprtid = models.AutoField(primary_key=True)
    relative_name = models.CharField(max_length=100)
    relative = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="relative")
    relationtype = models.ForeignKey(
        RelationType, on_delete=models.CASCADE)

    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="self")

    class Meta:
        managed = False
        db_table = 'memberprt'


class MemPersonal(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    mempersonalid = models.AutoField(primary_key=True)
    dob = models.DateTimeField(blank=True, null=True)
    bloodgroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    address = models.TextField()
    locality = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    yearlyincome = models.FloatField()
    resdidence = models.ForeignKey(ResidenceType, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'mempersonal'


class Qualification(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    qualificationid = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    university = models.CharField(max_length=255)
    passingyear = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qualification'


class Occupation(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    occupationid = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    occupationtype = models.ForeignKey(
        OccupationType, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    office_add = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'occupation'


class HealthSheet(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    healthsheetid = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    diesase = models.CharField(max_length=200)
    diagnose_dt = models.DateTimeField(default=timezone.now)
    doctor_consulted = models.CharField(max_length=200)
    treatment = models.TextField()
    cured = models.BooleanField(default=False, editable=False)

    class Meta:
        managed = False
        db_table = 'healthsheet'
