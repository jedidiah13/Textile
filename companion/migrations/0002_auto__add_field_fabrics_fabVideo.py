# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fabrics.fabVideo'
        db.add_column(u'companion_fabrics', 'fabVideo',
                      self.gf('embed_video.fields.EmbedVideoField')(default=0, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Fabrics.fabVideo'
        db.delete_column(u'companion_fabrics', 'fabVideo')


    models = {
        u'companion.catagories': {
            'Meta': {'object_name': 'Catagories'},
            'catagory': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'companion.fabrics': {
            'Meta': {'object_name': 'Fabrics'},
            'fabCatagory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companion.Catagories']"}),
            'fabContent': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabDescription': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'fabDye': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabFinish': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'fabName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabTopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companion.Topics']"}),
            'fabVideo': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'}),
            'fabWeave': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'companion.topics': {
            'Meta': {'object_name': 'Topics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['companion']