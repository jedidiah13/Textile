# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StoreItem.itemNameid'
        db.add_column(u'webstore_storeitem', 'itemNameid',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)


        # Changing field 'StoreItem.description'
        db.alter_column(u'webstore_storeitem', 'description', self.gf('django.db.models.fields.CharField')(max_length=2048))

    def backwards(self, orm):
        # Deleting field 'StoreItem.itemNameid'
        db.delete_column(u'webstore_storeitem', 'itemNameid')


        # Changing field 'StoreItem.description'
        db.alter_column(u'webstore_storeitem', 'description', self.gf('django.db.models.fields.CharField')(max_length=1024))

    models = {
        u'webstore.storecategory': {
            'Meta': {'object_name': 'StoreCategory'},
            'categoryName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webstore.storeitem': {
            'Meta': {'object_name': 'StoreItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.StoreCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'itemNameid': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['webstore']