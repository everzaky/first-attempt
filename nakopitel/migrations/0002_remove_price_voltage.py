# Generated by Django 2.1 on 2018-08-22 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nakopitel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='voltage',
        ),
    ]
