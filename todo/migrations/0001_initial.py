# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'List'
        db.create_table('todo_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=60, db_index=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'])),
        ))
        db.send_create_signal('todo', ['List'])

        # Adding unique constraint on 'List', fields ['group', 'slug']
        db.create_unique('todo_list', ['group_id', 'slug'])

        # Adding model 'Item'
        db.create_table('todo_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.List'])),
            ('created_date', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('completed_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_by', to=orm['auth.User'])),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='todo_assigned_to', to=orm['auth.User'])),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=3)),
        ))
        db.send_create_signal('todo', ['Item'])

        # Adding model 'Comment'
        db.create_table('todo_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.Item'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('todo', ['Comment'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'List', fields ['group', 'slug']
        db.delete_unique('todo_list', ['group_id', 'slug'])

        # Deleting model 'List'
        db.delete_table('todo_list')

        # Deleting model 'Item'
        db.delete_table('todo_item')

        # Deleting model 'Comment'
        db.delete_table('todo_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'todo.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.Item']"})
        },
        'todo.item': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Item'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todo_assigned_to'", 'to': "orm['auth.User']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_by'", 'to': "orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.List']"}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'todo.list': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('group', 'slug'),)", 'object_name': 'List'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '60', 'db_index': 'True'})
        }
    }

    complete_apps = ['todo']
