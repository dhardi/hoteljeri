# Generated by Django 4.2.11 on 2024-04-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_post_excerpt_post_updated_on_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_on"]},
        ),
    ]
