# Generated by Django 4.2.11 on 2024-04-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("rollno", models.CharField(max_length=100)),
            ],
        ),
    ]