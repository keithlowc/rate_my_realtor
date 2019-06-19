# Generated by Django 2.2.2 on 2019-06-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0007_auto_20190617_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default=None, max_length=250)),
                ('rate', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor.Agent')),
            ],
        ),
    ]