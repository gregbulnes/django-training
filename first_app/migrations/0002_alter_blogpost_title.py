# Generated by Django 4.1 on 2023-07-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=250),
        ),
    ]
