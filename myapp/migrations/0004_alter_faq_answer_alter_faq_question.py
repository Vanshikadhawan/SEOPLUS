# Generated by Django 5.0.2 on 2024-02-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_faq_latestnews_searchengine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="faq",
            name="question",
            field=models.TextField(),
        ),
    ]
