# Generated by Django 2.2.2 on 2019-06-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='something',
            field=models.BooleanField(default=False),
        ),
    ]