# Generated by Django 3.1.3 on 2020-11-08 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20201108_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Work',
            new_name='work',
        ),
    ]
