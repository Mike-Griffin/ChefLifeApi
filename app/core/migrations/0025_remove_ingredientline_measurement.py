# Generated by Django 3.1.3 on 2021-01-28 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210128_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientline',
            name='measurement',
        ),
    ]
