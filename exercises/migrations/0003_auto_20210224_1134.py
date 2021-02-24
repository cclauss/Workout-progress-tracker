# Generated by Django 3.1.6 on 2021-02-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_auto_20210224_1134'),
        ('exercises', '0002_auto_20210219_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='body_part',
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle',
            field=models.ManyToManyField(related_name='muscle', to='body.Muscle'),
        ),
    ]
