# Generated by Django 4.2.4 on 2023-08-30 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="description",
        ),
    ]