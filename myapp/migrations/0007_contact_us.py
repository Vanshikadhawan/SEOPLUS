# Generated by Django 5.0.2 on 2024-02-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_user_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact_us",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                ("message", models.TextField(max_length=500)),
            ],
        ),
    ]
