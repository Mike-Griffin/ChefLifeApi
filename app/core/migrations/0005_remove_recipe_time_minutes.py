# Generated by Django 3.1.3 on 2021-01-13 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='time_minutes',
        ),
    ]