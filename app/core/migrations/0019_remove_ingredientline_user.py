# Generated by Django 3.1.3 on 2021-01-25 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210125_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientline',
            name='user',
        ),
    ]
