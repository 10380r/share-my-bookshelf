# Generated by Django 3.0.5 on 2020-05-02 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200429_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='rabel',
            new_name='label',
        ),
    ]
