# Generated by Django 4.1.1 on 2022-09-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0012_alter_user_user_info"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_info",
        ),
    ]
