# Generated by Django 2.2.6 on 2020-01-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=300, verbose_name='Repository')),
                ('description', models.TextField()),
                ('pushed_at', models.DateTimeField()),
                ('url', models.URLField(max_length=400)),
                ('github_repo_id', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Repositories',
                'ordering': ['-pushed_at'],
            },
        ),
    ]
