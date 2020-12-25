# Generated by Django 3.1.3 on 2020-11-19 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_store', '0006_auto_20201119_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='coffee_store.item')),
                ('caffeine', models.IntegerField(null=True)),
            ],
        ),
    ]
