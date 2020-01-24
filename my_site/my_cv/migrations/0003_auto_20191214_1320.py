# Generated by Django 2.2.6 on 2019-12-14 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0002_auto_20191214_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienceoroutreach',
            name='duration',
        ),
        migrations.AddField(
            model_name='experienceoroutreach',
            name='current_position',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experienceoroutreach',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experienceoroutreach',
            name='position_title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experienceoroutreach',
            name='start_date',
            field=models.DateField(default=datetime.date(2019, 12, 14)),
            preserve_default=False,
        ),
    ]