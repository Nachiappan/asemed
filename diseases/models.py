from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
       return self.name

class Field(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
       return self.name

class Disease(models.Model):
    name = models.CharField(max_length=40)
    symptoms = models.ManyToManyField(Symptom, through='DiseaseSymptom')
    treatments = models.ManyToManyField('appointments.Treatment', through='appointments.DiseaseTreatment')
    field = models.ForeignKey(Field, null=True, blank=True)
    details = models.TextField()
    def __unicode__(self):
       return self.name

class DiseaseSymptom(models.Model):
    disease = models.ForeignKey(Disease)
    symptom = models.ForeignKey(Symptom)
    confidence_percent = models.PositiveIntegerField()
    def __unicode__(self):
       return str(self.disease) + " | " + str(self.symptom)
    class Meta:
       unique_together = ["disease", "symptom"]
