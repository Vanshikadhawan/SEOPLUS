# Generated by Django 5.0.2 on 2024-02-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0011_delete_userchangepassword"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_register",
            name="DOB",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="user_register",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user_register",
            name="contact",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="user_register",
            name="pincode",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
