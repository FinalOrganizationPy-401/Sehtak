# Generated by Django 4.1.1 on 2022-09-19 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visits", "0013_remove_visits_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="visits",
            name="medicine_status",
            field=models.BooleanField(default=False),
        ),
    ]
