# Generated by Django 5.0.7 on 2024-08-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0023_wishlist"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customeraddress",
            options={"verbose_name_plural": "Customer Addresses"},
        ),
        migrations.AlterModelOptions(
            name="orderitems",
            options={"verbose_name_plural": "Order Items"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name_plural": "Product Catagories"},
        ),
        migrations.AddField(
            model_name="customer",
            name="profile_img",
            field=models.ImageField(null=True, upload_to="profile_img/"),
        ),
    ]
