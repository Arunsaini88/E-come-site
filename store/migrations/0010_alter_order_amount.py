# Generated by Django 5.0.2 on 2024-02-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
