# Generated by Django 5.0.7 on 2024-08-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='serie_number',
        ),
    ]
