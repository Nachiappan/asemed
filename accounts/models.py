from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
   (u'M', u'Male'),
   (u'F', u'Female'),
)

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=60)
    city = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='patient_obj', null=True, blank=True)
    def __unicode__(self):
       return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    specialisations = models.ManyToManyField('diseases.Field' , null=True, blank=True)
    user = models.OneToOneField(User, related_name='doctor_obj', null=True, blank=True)
    def __unicode__(self):
       return self.name
