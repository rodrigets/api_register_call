# Generated by Django 2.0.5 on 2018-06-15 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20180615_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='call_code',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]
