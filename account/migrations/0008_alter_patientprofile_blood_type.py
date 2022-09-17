# Generated by Django 4.1.1 on 2022-09-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0007_alter_patientprofile_blood_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientprofile",
            name="blood_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("AB+", "AB+"),
                    ("AB-", "AB-"),
                    ("A+", "A+"),
                    ("A-", "A-"),
                    ("B+", "B+"),
                    ("B-", "B-"),
                    ("O+", "O+"),
                    ("O-", "O-"),
                ],
                default="AB+",
                max_length=50,
                null=True,
            ),
        ),
    ]
