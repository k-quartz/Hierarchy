from django.db import models
from django.utils import timezone


class Bloodgroup(models.Model):
    agre = models.TextField()  # This field type is a guess.
    reject = models.TextField()  # This field type is a guess.
    bloodgroup = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'bloodgroup'


class Member(models.Model):
    agre = models.BooleanField(default=False, editable=False)
    # This field type is a guess.
    reject = models.BooleanField(default=False, editable=False)
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
        managed = True
        db_table = 'member'


class RelationType(models.Model):
    agre = models.TextField()  # This field type is a guess.
    reject = models.TextField()  # This field type is a guess.
    relationtype = models.CharField(max_length=25)

    class Meta:
        managed = True
        db_table = 'relationtype'


class MemberPrt(models.Model):
    relative_name = models.CharField(max_length=100)
    relativeid = models.IntegerField()
    relation = models.ForeignKey(RelationType, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'memberprt'


class MemberPersonal(models.Model):
    agre = models.TextField()  # This field type is a guess.
    reject = models.TextField()  # This field type is a guess.
    dob = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    bloodgroup = models.ForeignKey(
        Bloodgroup, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'memberpersonal'
