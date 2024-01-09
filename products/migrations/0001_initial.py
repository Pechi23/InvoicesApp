# Generated by Django 5.0 on 2024-01-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=128)),
                (
                    "description",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("price", models.PositiveIntegerField()),
                ("UniqueId", models.CharField(max_length=16)),
                ("slug", models.SlugField()),
            ],
        ),
    ]
