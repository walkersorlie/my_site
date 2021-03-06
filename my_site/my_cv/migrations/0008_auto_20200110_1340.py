# Generated by Django 2.2.6 on 2020-01-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0007_resume_is_current_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='resume',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience',
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.ManyToManyField(blank=True, to='my_cv.ExperienceOrOutreach'),
        ),
        migrations.RemoveField(
            model_name='resume',
            name='personal_links',
        ),
        migrations.AddField(
            model_name='resume',
            name='personal_links',
            field=models.ManyToManyField(blank=True, to='my_cv.PersonalLink'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='University',
        ),
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.ManyToManyField(blank=True, to='my_cv.Education'),
        ),
    ]
