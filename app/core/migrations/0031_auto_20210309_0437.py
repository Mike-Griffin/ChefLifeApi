# Generated by Django 3.1.5 on 2021-03-09 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_testchildwithuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testchildwithuser',
            name='testparenttag_ptr',
        ),
        migrations.RemoveField(
            model_name='testchildwithuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='TestChildTag',
        ),
        migrations.DeleteModel(
            name='TestChildWithUser',
        ),
        migrations.DeleteModel(
            name='TestParentTag',
        ),
    ]
