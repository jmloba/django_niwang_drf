# Generated by Django 5.1.4 on 2025-01-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='image-default/no-image.png', null=True, upload_to='product_image/'),
        ),
    ]
