# Generated by Django 2.2.2 on 2019-06-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0009_auto_20190618_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='something',
            field=models.TextField(default='No Information', max_length=350),
        ),
    ]
