# Generated by Django 4.0.2 on 2022-02-11 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('std_portal', '0007_auto_20220211_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Financial',
            new_name='FinancialUni',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
