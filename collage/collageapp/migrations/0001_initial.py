# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collage'
        db.create_table(u'collageapp_collage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'collageapp', ['Collage'])

        # Adding model 'Postcard'
        db.create_table(u'collageapp_postcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('collage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collageapp.Collage'])),
        ))
        db.send_create_signal(u'collageapp', ['Postcard'])

        # Adding model 'Picture'
        db.create_table(u'collageapp_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tester', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'collageapp', ['Picture'])

        # Adding model 'PostcardPicture'
        db.create_table(u'collageapp_postcardpicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collageapp.Postcard'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collageapp.Picture'])),
        ))
        db.send_create_signal(u'collageapp', ['PostcardPicture'])


    def backwards(self, orm):
        # Deleting model 'Collage'
        db.delete_table(u'collageapp_collage')

        # Deleting model 'Postcard'
        db.delete_table(u'collageapp_postcard')

        # Deleting model 'Picture'
        db.delete_table(u'collageapp_picture')

        # Deleting model 'PostcardPicture'
        db.delete_table(u'collageapp_postcardpicture')


    models = {
        u'collageapp.collage': {
            'Meta': {'object_name': 'Collage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'collageapp.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tester': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'collageapp.postcard': {
            'Meta': {'object_name': 'Postcard'},
            'collage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collageapp.Collage']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'collageapp.postcardpicture': {
            'Meta': {'object_name': 'PostcardPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collageapp.Picture']"}),
            'postcard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collageapp.Postcard']"})
        }
    }

    complete_apps = ['collageapp']