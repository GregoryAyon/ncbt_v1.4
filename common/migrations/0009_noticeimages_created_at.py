# Generated by Django 4.0.2 on 2022-02-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_rename_studentregistrationcollage_noticeimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeimages',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]