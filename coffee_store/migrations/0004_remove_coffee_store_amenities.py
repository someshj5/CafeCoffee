# Generated by Django 3.1.3 on 2020-11-19 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_store', '0003_auto_20201119_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee_store',
            name='amenities',
        ),
    ]
