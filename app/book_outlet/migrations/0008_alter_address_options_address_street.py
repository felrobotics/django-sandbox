# Generated by Django 4.2.9 on 2024-01-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0007_address_author_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Address Entries"},
        ),
        migrations.AddField(
            model_name="address",
            name="street",
            field=models.CharField(max_length=80, null=True),
        ),
    ]