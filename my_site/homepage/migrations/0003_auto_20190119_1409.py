# Generated by Django 2.1.3 on 2019-01-19 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190119_1401'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RepositoryTest',
            new_name='Repository',
        ),
    ]