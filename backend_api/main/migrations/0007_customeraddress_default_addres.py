# Generated by Django 5.0.7 on 2024-07-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_customeraddress"),
    ]

    operations = [
        migrations.AddField(
            model_name="customeraddress",
            name="default_addres",
            field=models.BooleanField(default=False),
        ),
    ]
