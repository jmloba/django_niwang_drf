# Generated by Django 5.1.4 on 2025-01-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='admin_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='article_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='article_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='programmer_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='send_email_trigger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='todo_access_all',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='todo_rights',
            field=models.BooleanField(default=False),
        ),
    ]