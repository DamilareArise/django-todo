# Generated by Django 5.1.6 on 2025-03-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0003_alter_profile_passport"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="passport",
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(null=True, upload_to="picture/"),
        ),
    ]
