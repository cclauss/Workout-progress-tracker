# Generated by Django 3.1.6 on 2021-02-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_auto_20210226_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlog',
            name='short_note',
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='summary',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
