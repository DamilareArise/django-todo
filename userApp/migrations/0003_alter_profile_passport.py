# Generated by Django 5.1.6 on 2025-03-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0002_remove_profile_created_at_remove_profile_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="passport",
            field=models.ImageField(null=True, upload_to="passport/"),
        ),
    ]
