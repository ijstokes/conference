# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'schedule_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_day', self.gf('django.db.models.fields.DateField')()),
            ('end_day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'schedule', ['Section'])

        # Adding model 'Track'
        db.create_table(u'schedule_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'schedule', ['Track'])

        # Adding model 'TimeSlot'
        db.create_table(u'schedule_timeslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('sectionDay', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.SectionDay'])),
        ))
        db.send_create_signal(u'schedule', ['TimeSlot'])

        # Adding model 'SectionDay'
        db.create_table(u'schedule_sectionday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Section'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'schedule', ['SectionDay'])

        # Adding model 'RoomUseType'
        db.create_table(u'schedule_roomusetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'schedule', ['RoomUseType'])

        # Adding model 'Room'
        db.create_table(u'schedule_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('useType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.RoomUseType'])),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('map_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Room'])

        # Adding model 'ScheduledItemType'
        db.create_table(u'schedule_scheduleditemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'schedule', ['ScheduledItemType'])

        # Adding model 'ScheduledItem'
        db.create_table(u'schedule_scheduleditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.ScheduledItemType'])),
            ('timeSlot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.TimeSlot'])),
            ('num_slots', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Track'], null=True, blank=True)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Room'], null=True, blank=True)),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['speakers.Presentation'], null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['ScheduledItem'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'schedule_section')

        # Deleting model 'Track'
        db.delete_table(u'schedule_track')

        # Deleting model 'TimeSlot'
        db.delete_table(u'schedule_timeslot')

        # Deleting model 'SectionDay'
        db.delete_table(u'schedule_sectionday')

        # Deleting model 'RoomUseType'
        db.delete_table(u'schedule_roomusetype')

        # Deleting model 'Room'
        db.delete_table(u'schedule_room')

        # Deleting model 'ScheduledItemType'
        db.delete_table(u'schedule_scheduleditemtype')

        # Deleting model 'ScheduledItem'
        db.delete_table(u'schedule_scheduleditem')


    models = {
        u'events.conference': {
            'Meta': {'object_name': 'Conference'},
            'begin_date': ('django.db.models.fields.DateTimeField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'schedule.room': {
            'Meta': {'object_name': 'Room'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'useType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.RoomUseType']"})
        },
        u'schedule.roomusetype': {
            'Meta': {'object_name': 'RoomUseType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'schedule.scheduleditem': {
            'Meta': {'ordering': "['timeSlot', 'track']", 'object_name': 'ScheduledItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.ScheduledItemType']"}),
            'num_slots': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['speakers.Presentation']", 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Room']", 'null': 'True', 'blank': 'True'}),
            'timeSlot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.TimeSlot']"}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Track']", 'null': 'True', 'blank': 'True'})
        },
        u'schedule.scheduleditemtype': {
            'Meta': {'object_name': 'ScheduledItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'schedule.section': {
            'Meta': {'object_name': 'Section'},
            'end_day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_day': ('django.db.models.fields.DateField', [], {})
        },
        u'schedule.sectionday': {
            'Meta': {'ordering': "['day']", 'object_name': 'SectionDay'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Section']"})
        },
        u'schedule.timeslot': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'TimeSlot'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sectionDay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.SectionDay']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'schedule.track': {
            'Meta': {'object_name': 'Track'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'speakers.presentation': {
            'Meta': {'ordering': "['title']", 'object_name': 'Presentation'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'additional_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Conference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['speakers.Speaker']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'speakers.speaker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']