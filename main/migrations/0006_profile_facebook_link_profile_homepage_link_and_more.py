# Generated by Django 5.0.2 on 2024-03-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_tweet_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="homepage_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="instagram_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkedin_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_bio",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]