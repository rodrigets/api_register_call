# Generated by Django 2.0.5 on 2018-06-15 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_remove_register_call_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='time',
            new_name='call_datetime',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='destination',
            new_name='destine_number',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='source',
            new_name='source_number',
        ),
    ]
