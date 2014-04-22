# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fabrics.fabImage_secondary'
        db.add_column(u'companion_fabrics', 'fabImage_secondary',
                      self.gf('imagekit.models.fields.ProcessedImageField')(default=0, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Fabrics.isPremium'
        db.add_column(u'companion_fabrics', 'isPremium',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Fabrics.fabImage'
        db.alter_column(u'companion_fabrics', 'fabImage', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Fabrics.fabImage_secondary'
        db.delete_column(u'companion_fabrics', 'fabImage_secondary')

        # Deleting field 'Fabrics.isPremium'
        db.delete_column(u'companion_fabrics', 'isPremium')


        # Changing field 'Fabrics.fabImage'
        db.alter_column(u'companion_fabrics', 'fabImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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
            'fabImage': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'fabImage_secondary': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'blank': 'True'}),
            'fabName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'fabTopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companion.Topics']"}),
            'fabVideo': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'}),
            'fabWeave': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isPremium': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'companion.topics': {
            'Meta': {'object_name': 'Topics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['companion']