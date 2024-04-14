# Generated by Django 4.2.7 on 2024-01-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopFront", "0008_alter_order_payment_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="note",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="membership",
            field=models.CharField(
                choices=[("BRONZE", "BRONZE"), ("SILVER", "SILVER"), ("GOLD", "GOLD")],
                default="BRONZE",
                max_length=6,
            ),
        ),
    ]
