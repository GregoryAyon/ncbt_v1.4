# Generated by Django 4.0.2 on 2022-02-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_portal', '0009_auto_20220214_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistrationuni',
            name='cgpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentregistrationcollage',
            name='student_id',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentregistrationuni',
            name='student_id',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
