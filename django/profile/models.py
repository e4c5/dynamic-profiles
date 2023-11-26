from django.db import models
from countries.models import Country

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    gender_choices = [('M','MALE'),('F','FEMALE'), ('U','UNSPECIFIED')]
    national_id =  models.CharField(max_length=16)
    passport =  models.CharField(max_length=16)
    country =  models.ForeignKey(Country, null=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    third_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=gender_choices)
    is_active = models.BooleanField(default=True)
    bio = models.CharField(max_length=1024)

    class Meta:
        unique_together = [
            ['national_id','country'],
            ['passport','country']
        ]

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(Person, null=False, blank=False, on_delete=models.PROTECT)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address1 = models.CharField(max_length=64)
    address2 = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    extra_data = models.JSONField(default=dict, null=False, blank=True)

