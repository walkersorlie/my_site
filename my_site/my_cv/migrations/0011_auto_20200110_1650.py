# Generated by Django 2.2.6 on 2020-01-10 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0010_auto_20200110_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='last_edited',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
