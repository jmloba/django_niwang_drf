# Generated by Django 5.1.4 on 2025-01-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_productcategory_product_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
