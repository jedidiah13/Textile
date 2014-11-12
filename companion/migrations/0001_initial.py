# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Catagories'
        db.create_table(u'companion_catagories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catagory', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('categoryId', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'companion', ['Catagories'])

        # Adding model 'Topics'
        db.create_table(u'companion_topics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fabCatagory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companion.Catagories'])),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('topicId', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'companion', ['Topics'])

        # Adding model 'Fabrics'
        db.create_table(u'companion_fabrics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fabTopic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companion.Topics'])),
            ('fabName', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabContent', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('fabWeave', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('fabDye', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('fabFinish', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('fabDescription', self.gf('django.db.models.fields.CharField')(max_length=8192)),
            ('fabImage', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, blank=True)),
            ('fabImage_secondary', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, blank=True)),
            ('fabVideo', self.gf('embed_video.fields.EmbedVideoField')(max_length=200, blank=True)),
            ('fabVideoURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('isPremium', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'companion', ['Fabrics'])


    def backwards(self, orm):
        # Deleting model 'Catagories'
        db.delete_table(u'companion_catagories')

        # Deleting model 'Topics'
        db.delete_table(u'companion_topics')

        # Deleting model 'Fabrics'
        db.delete_table(u'companion_fabrics')


    models = {
        u'companion.catagories': {
            'Meta': {'object_name': 'Catagories'},
            'catagory': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'categoryId': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'companion.fabrics': {
            'Meta': {'object_name': 'Fabrics'},
            'fabContent': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'fabDescription': ('django.db.models.fields.CharField', [], {'max_length': '8192'}),
            'fabDye': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'fabFinish': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'fabImage': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'fabImage_secondary': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'fabName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabTopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companion.Topics']"}),
            'fabVideo': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200', 'blank': 'True'}),
            'fabVideoURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'fabWeave': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isPremium': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'companion.topics': {
            'Meta': {'object_name': 'Topics'},
            'fabCatagory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companion.Catagories']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'topicId': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['companion']