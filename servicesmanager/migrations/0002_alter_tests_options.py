# Generated by Django 4.1.1 on 2022-09-10 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("servicesmanager", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tests",
            options={"verbose_name": "Test", "verbose_name_plural": "Tests"},
        ),
    ]
