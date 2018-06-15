# Generated by Django 2.0.6 on 2018-06-15 11:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='call_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Register'),
        ),
        migrations.AlterField(
            model_name='register',
            name='destination',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='register',
            name='source',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(8)]),
        ),
    ]
