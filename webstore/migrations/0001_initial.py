# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoreCategory'
        db.create_table(u'webstore_storecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoryName', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'webstore', ['StoreCategory'])

        # Adding model 'StoreItem'
        db.create_table(u'webstore_storeitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.StoreCategory'])),
            ('itemName', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('itemNameid', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('picture', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('featured_picture', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, blank=True)),
            ('isFeatured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('canCalcShipping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weightPerItem', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('numberPerBox', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('boxWidth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('boxDepth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('boxHeight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('isFabric', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isSmallItem', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isSwatchKit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isFeltingKit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'webstore', ['StoreItem'])

        # Adding model 'Order'
        db.create_table(u'webstore_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purchaser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['login.UserProfile'], null=True)),
            ('orderDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('shippingCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('totalCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
        ))
        db.send_create_signal(u'webstore', ['Order'])

        # Adding model 'OrderItemCorrect'
        db.create_table(u'webstore_orderitemcorrect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemCost', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('itemQuantity', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Order'], null=True)),
            ('itemID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.StoreItem'], null=True)),
        ))
        db.send_create_signal(u'webstore', ['OrderItemCorrect'])


    def backwards(self, orm):
        # Deleting model 'StoreCategory'
        db.delete_table(u'webstore_storecategory')

        # Deleting model 'StoreItem'
        db.delete_table(u'webstore_storeitem')

        # Deleting model 'Order'
        db.delete_table(u'webstore_order')

        # Deleting model 'OrderItemCorrect'
        db.delete_table(u'webstore_orderitemcorrect')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'login.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'State': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address_lineOne': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address_lineTwo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'appExpiryDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'webstore.order': {
            'Meta': {'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orderDate': ('django.db.models.fields.DateTimeField', [], {}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['login.UserProfile']", 'null': 'True'}),
            'shippingCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'totalCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        u'webstore.orderitemcorrect': {
            'Meta': {'object_name': 'OrderItemCorrect'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'itemID': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.StoreItem']", 'null': 'True'}),
            'itemQuantity': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Order']", 'null': 'True'})
        },
        u'webstore.storecategory': {
            'Meta': {'object_name': 'StoreCategory'},
            'categoryName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'webstore.storeitem': {
            'Meta': {'object_name': 'StoreItem'},
            'boxDepth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'boxHeight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'boxWidth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'canCalcShipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.StoreCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'featured_picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFabric': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isFeatured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isFeltingKit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSmallItem': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isSwatchKit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itemName': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'itemNameid': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numberPerBox': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weightPerItem': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['webstore']