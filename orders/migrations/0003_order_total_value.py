# Generated by Django 5.0.7 on 2024-08-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
    ]
