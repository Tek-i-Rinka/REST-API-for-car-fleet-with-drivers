# Generated by Django 4.0 on 2021-12-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='driver_id',
            field=models.ForeignKey(on_delete=models.SET(0), to='ParkApp.drivers'),
        ),
    ]
