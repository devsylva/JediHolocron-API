# Generated by Django 4.2.4 on 2023-08-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_comment_film"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="comment_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
