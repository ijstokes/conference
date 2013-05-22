# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SponsorLevel'
        db.create_table(u'sponsors_sponsorlevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('min_amount', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Conference'])),
            ('small_logo_height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sponsors', ['SponsorLevel'])

        # Adding model 'Sponsor'
        db.create_table(u'sponsors_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsors', to=orm['sponsors.SponsorLevel'])),
            ('logo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'sponsors', ['Sponsor'])


    def backwards(self, orm):
        # Deleting model 'SponsorLevel'
        db.delete_table(u'sponsors_sponsorlevel')

        # Deleting model 'Sponsor'
        db.delete_table(u'sponsors_sponsor')


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
        u'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': u"orm['sponsors.SponsorLevel']"}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sponsors.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Conference']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_amount': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'small_logo_height': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sponsors']