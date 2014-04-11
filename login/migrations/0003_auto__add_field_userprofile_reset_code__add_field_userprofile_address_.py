# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.reset_code'
        db.add_column(u'login_userprofile', 'reset_code',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)

        # Adding field 'UserProfile.address_lineOne'
        db.add_column(u'login_userprofile', 'address_lineOne',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)

        # Adding field 'UserProfile.address_lineTwo'
        db.add_column(u'login_userprofile', 'address_lineTwo',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)

        # Adding field 'UserProfile.city'
        db.add_column(u'login_userprofile', 'city',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)

        # Adding field 'UserProfile.State'
        db.add_column(u'login_userprofile', 'State',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=128),
                      keep_default=False)

        # Adding field 'UserProfile.zipCode'
        db.add_column(u'login_userprofile', 'zipCode',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.reset_code'
        db.delete_column(u'login_userprofile', 'reset_code')

        # Deleting field 'UserProfile.address_lineOne'
        db.delete_column(u'login_userprofile', 'address_lineOne')

        # Deleting field 'UserProfile.address_lineTwo'
        db.delete_column(u'login_userprofile', 'address_lineTwo')

        # Deleting field 'UserProfile.city'
        db.delete_column(u'login_userprofile', 'city')

        # Deleting field 'UserProfile.State'
        db.delete_column(u'login_userprofile', 'State')

        # Deleting field 'UserProfile.zipCode'
        db.delete_column(u'login_userprofile', 'zipCode')


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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['login']