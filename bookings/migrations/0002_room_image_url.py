# Generated by Django 5.0.5 on 2024-05-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="image_url",
            field=models.URLField(blank=True),
        ),
    ]
