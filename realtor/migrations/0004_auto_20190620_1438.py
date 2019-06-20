# Generated by Django 2.2.2 on 2019-06-20 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0003_auto_20190620_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentsdata',
            name='comments',
            field=models.TextField(default=None, max_length=350),
        ),
        migrations.AlterField(
            model_name='agentsdata',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
