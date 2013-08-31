# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Picture.tester'
        db.delete_column(u'collageapp_picture', 'tester')


    def backwards(self, orm):
        # Adding field 'Picture.tester'
        db.add_column(u'collageapp_picture', 'tester',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100),
                      keep_default=False)


    models = {
        u'collageapp.collage': {
            'Meta': {'object_name': 'Collage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'collageapp.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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