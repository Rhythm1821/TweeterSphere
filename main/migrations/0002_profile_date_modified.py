# Generated by Django 5.0.2 on 2024-02-28 10:45

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]
