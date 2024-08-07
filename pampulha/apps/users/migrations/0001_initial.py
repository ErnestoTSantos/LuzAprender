# Generated by Django 4.0.3 on 2024-07-05 19:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsychologistModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Identificador do usuário')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('age', models.IntegerField(verbose_name='Idade')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=15, verbose_name='Gênero')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated date')),
            ],
            options={
                'verbose_name': 'Psychologist',
                'verbose_name_plural': 'Psychologists',
            },
        ),
    ]
