# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Appointment'
        db.create_table('appointments_appointment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Patient'])),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Doctor'])),
            ('appointment_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('appointments', ['Appointment'])

        # Adding model 'Treatment'
        db.create_table('appointments_treatment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('appointments', ['Treatment'])

        # Adding model 'DiseaseTreatment'
        db.create_table('appointments_diseasetreatment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disease', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diseases.Disease'])),
            ('treatment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appointments.Treatment'])),
            ('confidence_percent', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('appointments', ['DiseaseTreatment'])

        # Adding unique constraint on 'DiseaseTreatment', fields ['disease', 'treatment']
        db.create_unique('appointments_diseasetreatment', ['disease_id', 'treatment_id'])

        # Adding model 'Report'
        db.create_table('appointments_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appointment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appointments.Appointment'], unique=True)),
            ('disease_diagnosed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diseases.Disease'])),
        ))
        db.send_create_signal('appointments', ['Report'])

        # Adding M2M table for field symptoms_reported on 'Report'
        db.create_table('appointments_report_symptoms_reported', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm['appointments.report'], null=False)),
            ('symptom', models.ForeignKey(orm['diseases.symptom'], null=False))
        ))
        db.create_unique('appointments_report_symptoms_reported', ['report_id', 'symptom_id'])

        # Adding M2M table for field treatments on 'Report'
        db.create_table('appointments_report_treatments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('report', models.ForeignKey(orm['appointments.report'], null=False)),
            ('treatment', models.ForeignKey(orm['appointments.treatment'], null=False))
        ))
        db.create_unique('appointments_report_treatments', ['report_id', 'treatment_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'DiseaseTreatment', fields ['disease', 'treatment']
        db.delete_unique('appointments_diseasetreatment', ['disease_id', 'treatment_id'])

        # Deleting model 'Appointment'
        db.delete_table('appointments_appointment')

        # Deleting model 'Treatment'
        db.delete_table('appointments_treatment')

        # Deleting model 'DiseaseTreatment'
        db.delete_table('appointments_diseasetreatment')

        # Deleting model 'Report'
        db.delete_table('appointments_report')

        # Removing M2M table for field symptoms_reported on 'Report'
        db.delete_table('appointments_report_symptoms_reported')

        # Removing M2M table for field treatments on 'Report'
        db.delete_table('appointments_report_treatments')


    models = {
        'accounts.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'specialisations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['diseases.Field']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'doctor_obj'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'accounts.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'patient_obj'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'appointments.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'appointment_date': ('django.db.models.fields.DateTimeField', [], {}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Patient']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'appointments.diseasetreatment': {
            'Meta': {'unique_together': "(['disease', 'treatment'],)", 'object_name': 'DiseaseTreatment'},
            'confidence_percent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Disease']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['appointments.Treatment']"})
        },
        'appointments.report': {
            'Meta': {'object_name': 'Report'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointments.Appointment']", 'unique': 'True'}),
            'disease_diagnosed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['diseases.Disease']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'symptoms_reported': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['diseases.Symptom']", 'symmetrical': 'False'}),
            'treatments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['appointments.Treatment']", 'symmetrical': 'False'})
        },
        'appointments.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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

    complete_apps = ['appointments']
