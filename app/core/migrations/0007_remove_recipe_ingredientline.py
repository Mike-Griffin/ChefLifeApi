# Generated by Django 3.1.3 on 2021-01-25 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210125_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredientLine',
        ),
    ]
