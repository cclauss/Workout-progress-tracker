# Generated by Django 3.1.6 on 2021-02-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20210224_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='reps_unit',
            field=models.CharField(choices=[('RE', 'Reps'), ('UF', 'Until Failure')], default='RE', max_length=2),
        ),
    ]
