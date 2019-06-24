# Generated by Django 2.2.2 on 2019-06-20 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0005_auto_20190620_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentsdata',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]