# Generated by Django 5.0.7 on 2024-07-17 12:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_product_category_product_vender"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Vender",
            new_name="Vendor",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="vender",
            new_name="vendor",
        ),
    ]
