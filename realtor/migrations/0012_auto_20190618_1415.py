# Generated by Django 2.2.2 on 2019-06-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0011_auto_20190618_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='about',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='agent',
            name='rating',
            field=models.FloatField(),
        ),
    ]