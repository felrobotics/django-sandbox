# Generated by Django 4.2.9 on 2024-01-25 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0006_alter_book_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("postal_code", models.CharField(max_length=5)),
                ("city", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="author",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="book_outlet.address",
            ),
        ),
    ]