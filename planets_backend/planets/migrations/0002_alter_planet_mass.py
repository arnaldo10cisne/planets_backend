# Generated by Django 4.2.2 on 2023-09-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="planet",
            name="mass",
            field=models.CharField(max_length=256),
        ),
    ]
