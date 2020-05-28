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


class RelationType(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    relationtypeid = models.AutoField(primary_key=True)
    relationtype = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'relationtype'


class MemPersonal(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    reject = models.BooleanField(default=False, editable=False)
    mempersonalid = models.AutoField(primary_key=True)
    dob = models.DateTimeField(blank=True, null=True)
    bloodgroup = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mempersonal'


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
