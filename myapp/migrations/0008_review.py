# Generated by Django 5.0.2 on 2024-02-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_contact_us"),
    ]

    operations = [
        migrations.CreateModel(
            name="review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("message", models.TextField(max_length=500)),
            ],
        ),
    ]