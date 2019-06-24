# Generated by Django 2.2.2 on 2019-06-21 03:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0006_auto_20190620_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]