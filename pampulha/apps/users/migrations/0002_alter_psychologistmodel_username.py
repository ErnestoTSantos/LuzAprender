# Generated by Django 4.0.3 on 2023-06-07 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psychologistmodel',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Username'),
        ),
    ]
