# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SectionDay.conference'
        db.add_column(u'schedule_sectionday', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)

        # Adding field 'Section.conference'
        db.add_column(u'schedule_section', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)

        # Adding field 'ScheduledItem.conference'
        db.add_column(u'schedule_scheduleditem', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)

        # Adding field 'TimeSlot.conference'
        db.add_column(u'schedule_timeslot', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)

        # Adding field 'Track.conference'
        db.add_column(u'schedule_track', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)

        # Adding field 'Room.conference'
        db.add_column(u'schedule_room', 'conference',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Conference']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SectionDay.conference'
        db.delete_column(u'schedule_sectionday', 'conference_id')

        # Deleting field 'Section.conference'
        db.delete_column(u'schedule_section', 'conference_id')

        # Deleting field 'ScheduledItem.conference'
        db.delete_column(u'schedule_scheduleditem', 'conference_id')

        # Deleting field 'TimeSlot.conference'
        db.delete_column(u'schedule_timeslot', 'conference_id')

        # Deleting field 'Track.conference'
        db.delete_column(u'schedule_track', 'conference_id')

        # Deleting field 'Room.conference'
        db.delete_column(u'schedule_room', 'conference_id')


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
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
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
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
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
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
            'end_day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_day': ('django.db.models.fields.DateField', [], {})
        },
        u'schedule.sectionday': {
            'Meta': {'ordering': "['day']", 'object_name': 'SectionDay'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Section']"})
        },
        u'schedule.timeslot': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'TimeSlot'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sectionDay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.SectionDay']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'schedule.track': {
            'Meta': {'object_name': 'Track'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
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
