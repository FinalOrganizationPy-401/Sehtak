# Generated by Django 4.1.1 on 2022-09-17 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0009_remove_patientprofile_user_user_user_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_info",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="account.patientprofile",
            ),
        ),
    ]
