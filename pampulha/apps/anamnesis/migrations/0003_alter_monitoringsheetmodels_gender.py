# Generated by Django 4.0.3 on 2024-07-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0002_rename_first_contact_with_chest_anamnesismodels_first_contact_with_chest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringsheetmodels',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Feminino')], max_length=6, verbose_name='Sexo'),
        ),
    ]
