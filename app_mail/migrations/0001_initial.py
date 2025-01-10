# Generated by Django 5.1.4 on 2025-01-10 09:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailANS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.CharField(blank=True, max_length=50, null=True)),
                ('email_to', models.CharField(blank=True, max_length=50, null=True)),
                ('email_body', models.TextField(blank=True, max_length=400, null=True)),
                ('email_ref_id', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('package_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.CharField(blank=True, max_length=50, null=True)),
                ('email_to', models.CharField(blank=True, max_length=50, null=True)),
                ('email_body', models.TextField(blank=True, max_length=400, null=True)),
                ('replied', models.BooleanField(blank=True, default=False, null=True)),
                ('replied_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
