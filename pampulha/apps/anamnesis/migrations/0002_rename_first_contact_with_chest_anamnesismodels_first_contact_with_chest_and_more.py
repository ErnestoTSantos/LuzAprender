# Generated by Django 4.0.3 on 2024-06-27 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anamnesismodels',
            old_name='First_contact_with_chest',
            new_name='first_contact_with_chest',
        ),
        migrations.RenameField(
            model_name='monitoringsheetmodels',
            old_name='sex',
            new_name='gender',
        ),
    ]
