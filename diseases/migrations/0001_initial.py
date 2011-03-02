# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Symptom'
        db.create_table('diseases_symptom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('diseases', ['Symptom'])

        # Adding model 'Field'
        db.create_table('diseases_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('diseases', ['Field'])

        # Adding model 'Disease'
        db.create_table('diseases_disease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diseases.Field'], null=True, blank=True)),
            ('details', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('diseases', ['Disease'])

        # Adding model 'DiseaseSymptom'
        db.create_table('diseases_diseasesymptom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disease', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diseases.Disease'])),
            ('symptom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diseases.Symptom'])),
            ('confidence_percent', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('diseases', ['DiseaseSymptom'])

        # Adding unique constraint on 'DiseaseSymptom', fields ['disease', 'symptom']
        db.create_unique('diseases_diseasesymptom', ['disease_id', 'symptom_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'DiseaseSymptom', fields ['disease', 'symptom']
        db.delete_unique('diseases_diseasesymptom', ['disease_id', 'symptom_id'])

        # Deleting model 'Symptom'
        db.delete_table('diseases_symptom')

        # Deleting model 'Field'
        db.delete_table('diseases_field')

        # Deleting model 'Disease'
        db.delete_table('diseases_disease')

        # Deleting model 'DiseaseSymptom'
        db.delete_table('diseases_diseasesymptom')


    models = {
        'appointments.diseasetreatment': {
            'Meta': {'unique_together': "(['disease', 'treatment'],)", 'object_name': 'DiseaseTreatment'},
            'confidence_percent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Disease']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['appointments.Treatment']"})
        },
        'appointments.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'diseases.disease': {
            'Meta': {'object_name': 'Disease'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Field']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'symptoms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diseases.Symptom']", 'through': "orm['diseases.DiseaseSymptom']", 'symmetrical': 'False'}),
            'treatments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['appointments.Treatment']", 'through': "orm['appointments.DiseaseTreatment']", 'symmetrical': 'False'})
        },
        'diseases.diseasesymptom': {
            'Meta': {'unique_together': "(['disease', 'symptom'],)", 'object_name': 'DiseaseSymptom'},
            'confidence_percent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Disease']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'symptom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Symptom']"})
        },
        'diseases.field': {
            'Meta': {'object_name': 'Field'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'diseases.symptom': {
            'Meta': {'object_name': 'Symptom'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['diseases']
