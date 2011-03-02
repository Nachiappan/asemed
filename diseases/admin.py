from django.contrib import admin
from models import *

class DiseaseSymptomInline(admin.TabularInline):
   model = DiseaseSymptom

class DiseaseAdmin(admin.ModelAdmin):
   model = Disease
   search_fields = ['name']
   inlines = [DiseaseSymptomInline]

admin.site.register(Symptom)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(DiseaseSymptom)
admin.site.register(Field)
