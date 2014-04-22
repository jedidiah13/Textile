# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Catagories.categoryId'
        db.add_column(u'companion_catagories', 'categoryId',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Catagories.categoryId'
        db.delete_column(u'companion_catagories', 'categoryId')


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