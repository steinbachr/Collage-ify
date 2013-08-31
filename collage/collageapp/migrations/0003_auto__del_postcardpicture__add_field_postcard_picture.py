# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PostcardPicture'
        db.delete_table(u'collageapp_postcardpicture')

        # Adding field 'Postcard.picture'
        db.add_column(u'collageapp_postcard', 'picture',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['collageapp.Picture']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PostcardPicture'
        db.create_table(u'collageapp_postcardpicture', (
            ('postcard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collageapp.Postcard'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collageapp.Picture'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'collageapp', ['PostcardPicture'])

        # Deleting field 'Postcard.picture'
        db.delete_column(u'collageapp_postcard', 'picture_id')


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
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collageapp.Picture']"}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['collageapp']