# Generated by Django 5.0.7 on 2024-08-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflow',
            name='update_at',
        ),
        migrations.AddField(
            model_name='inflow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
