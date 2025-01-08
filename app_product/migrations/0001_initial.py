# Generated by Django 5.1.4 on 2025-01-07 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
