# Generated by Django 5.0.7 on 2024-08-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0018_order_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_file",
            field=models.FileField(null=True, upload_to="product_file/"),
        ),
    ]
