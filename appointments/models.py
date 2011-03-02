from django.db import models

APPOINTMENT_STATUS_CHOICES = (
   ('A', 'Accepted'),
   ('P', 'Pending'),
   ('R', 'Rejected'),
)

class Appointment(models.Model):
    patient = models.ForeignKey('accounts.Patient')
    doctor = models.ForeignKey('accounts.Doctor')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=APPOINTMENT_STATUS_CHOICES)
    def __unicode__(self):
       return str(self.patient) + " appointment with " + str(self.doctor)

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
       return self.name

class DiseaseTreatment(models.Model):
    disease = models.ForeignKey('diseases.Disease')
    treatment = models.ForeignKey(Treatment)
    confidence_percent = models.PositiveIntegerField()
    def __unicode__(self):
       return str(self.disease) + " | " + str(self.treatment)
    class Meta:
       unique_together = ["disease", "treatment"]

class Report(models.Model):
    appointment = models.OneToOneField(Appointment)
    symptoms_reported = models.ManyToManyField('diseases.Symptom')
    disease_diagnosed = models.ForeignKey('diseases.Disease')
    treatments = models.ManyToManyField(Treatment)
    def __unicode__(self):
       return "Report of " + str(self.appointment)

