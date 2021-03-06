# Generated by Django 2.0.5 on 2018-06-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20180615_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='call_type',
            field=models.CharField(choices=[('Start', 'start'), ('Stop', 'stop')], max_length=5),
        ),
        migrations.AlterField(
            model_name='register',
            name='destination',
            field=models.PositiveIntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='register',
            name='source',
            field=models.PositiveIntegerField(max_length=9),
        ),
    ]
