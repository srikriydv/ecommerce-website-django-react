# Generated by Django 5.0.7 on 2024-08-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_rename_tag_product_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
