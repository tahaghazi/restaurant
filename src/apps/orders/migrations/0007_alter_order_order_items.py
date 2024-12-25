# Generated by Django 4.2.17 on 2024-12-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0006_alter_order_table_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_items",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="cart", to="orders.orderitem"
            ),
        ),
    ]
