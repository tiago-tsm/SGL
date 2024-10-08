# Generated by Django 5.0.7 on 2024-08-16 01:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('enterprise', models.CharField(max_length=500)),
                ('telephone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Número de telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX', regex='^\\(\\d{2}\\) \\d{4,5}-\\d{4}$')])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
