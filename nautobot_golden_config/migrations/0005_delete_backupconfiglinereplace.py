# Generated by Django 3.1.7 on 2021-04-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_golden_config", "0004_auto_20210414_1757"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BackupConfigLineReplace",
        ),
    ]
