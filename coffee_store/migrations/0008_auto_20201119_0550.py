# Generated by Django 3.1.3 on 2020-11-19 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_store', '0007_drink'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='amenity',
            table='amenity',
        ),
        migrations.AlterModelTable(
            name='drink',
            table='drink',
        ),
        migrations.AlterModelTable(
            name='item',
            table='item',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu',
        ),
    ]