# Generated by Django 3.0.8 on 2020-07-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='to_address',
        ),
    ]
