# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teachers'
        db.create_table(u'api_teachers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Teachers'])

        # Adding model 'Subjects'
        db.create_table(u'api_subjects', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Subjects'])

        # Adding model 'Spiciality'
        db.create_table(u'api_spiciality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Spiciality'])

        # Adding model 'Groups'
        db.create_table(u'api_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('spec_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Spiciality'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('course', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Groups'])

        # Adding model 'Rooms'
        db.create_table(u'api_rooms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seats', self.gf('django.db.models.fields.IntegerField')()),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('is_computer_room', self.gf('django.db.models.fields.BooleanField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Rooms'])

        # Adding model 'Schedule'
        db.create_table(u'api_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Rooms'])),
            ('teacher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Teachers'])),
            ('subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Subjects'])),
            ('group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Groups'])),
            ('from_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('to_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_full_time', self.gf('django.db.models.fields.BooleanField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Schedule'])


    def backwards(self, orm):
        # Deleting model 'Teachers'
        db.delete_table(u'api_teachers')

        # Deleting model 'Subjects'
        db.delete_table(u'api_subjects')

        # Deleting model 'Spiciality'
        db.delete_table(u'api_spiciality')

        # Deleting model 'Groups'
        db.delete_table(u'api_groups')

        # Deleting model 'Rooms'
        db.delete_table(u'api_rooms')

        # Deleting model 'Schedule'
        db.delete_table(u'api_schedule')


    models = {
        u'api.groups': {
            'Meta': {'object_name': 'Groups'},
            'course': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'spec_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Spiciality']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'api.rooms': {
            'Meta': {'object_name': 'Rooms'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_computer_room': ('django.db.models.fields.BooleanField', [], {}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'seats': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'api.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_date': ('django.db.models.fields.DateTimeField', [], {}),
            'group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Groups']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_full_time': ('django.db.models.fields.BooleanField', [], {}),
            'room_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Rooms']"}),
            'subject_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Subjects']"}),
            'teacher_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Teachers']"}),
            'to_date': ('django.db.models.fields.DateTimeField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'api.spiciality': {
            'Meta': {'object_name': 'Spiciality'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'api.subjects': {
            'Meta': {'object_name': 'Subjects'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'api.teachers': {
            'Meta': {'object_name': 'Teachers'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['api']