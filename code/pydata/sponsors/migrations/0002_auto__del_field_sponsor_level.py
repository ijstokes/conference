# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sponsor.level'
        db.delete_column(u'sponsors_sponsor', 'level_id')

        # Adding M2M table for field sponsors on 'SponsorLevel'
        m2m_table_name = db.shorten_name(u'sponsors_sponsorlevel_sponsors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sponsorlevel', models.ForeignKey(orm[u'sponsors.sponsorlevel'], null=False)),
            ('sponsor', models.ForeignKey(orm[u'sponsors.sponsor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sponsorlevel_id', 'sponsor_id'])


    def backwards(self, orm):
        # Adding field 'Sponsor.level'
        db.add_column(u'sponsors_sponsor', 'level',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='sponsors', to=orm['sponsors.SponsorLevel']),
                      keep_default=False)

        # Removing M2M table for field sponsors on 'SponsorLevel'
        db.delete_table(db.shorten_name(u'sponsors_sponsorlevel_sponsors'))


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
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sponsors.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['events.Conference']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_amount': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'small_logo_height': ('django.db.models.fields.IntegerField', [], {}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sponsors.Sponsor']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['sponsors']
