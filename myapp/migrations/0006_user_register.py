# Generated by Django 5.0.2 on 2024-02-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_remove_blogs_des_remove_blogs_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_register",
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
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=40)),
            ],
        ),
    ]
