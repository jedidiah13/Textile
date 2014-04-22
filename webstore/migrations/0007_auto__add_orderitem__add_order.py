# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderItem'
        db.create_table(u'webstore_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('itemQuantity', self.gf('django.db.models.fields.IntegerField')()),
            ('itemID', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['webstore.StoreItem'], unique=True)),
        ))
        db.send_create_signal(u'webstore', ['OrderItem'])

        # Adding model 'Order'
        db.create_table(u'webstore_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orderDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('shippingCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('totalCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.OrderItem'])),
        ))
        db.send_create_signal(u'webstore', ['Order'])


    def backwards(self, orm):
        # Deleting model 'OrderItem'
        db.delete_table(u'webstore_orderitem')

        # Deleting model 'Order'
        db.delete_table(u'webstore_order')


    models = {
        u'webstore.order': {
            'Meta': {'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.OrderItem']"}),
            'orderDate': ('django.db.models.fields.DateTimeField', [], {}),
            'shippingCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'totalCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        u'webstore.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'itemID': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['webstore.StoreItem']", 'unique': 'True'}),
            'itemQuantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'webstore.storecategory': {
            'Meta': {'object_name': 'StoreCategory'},
            'categoryName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webstore.storeitem': {
            'Meta': {'object_name': 'StoreItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.StoreCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'featured_picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFeatured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itemName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'itemNameid': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['webstore']