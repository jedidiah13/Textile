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
        ))
        db.send_create_signal(u'companion', ['Catagories'])

        # Adding model 'Topics'
        db.create_table(u'companion_topics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'companion', ['Topics'])

        # Adding model 'Fabrics'
        db.create_table(u'companion_fabrics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fabCatagory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companion.Catagories'])),
            ('fabTopic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companion.Topics'])),
            ('fabName', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabContent', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabWeave', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabDye', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabFinish', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('fabDescription', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('fabImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
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