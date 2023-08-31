# Generated by Django 4.2.4 on 2023-08-31 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_comment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="film",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="core.film",
            ),
        ),
    ]
