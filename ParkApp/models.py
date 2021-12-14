from django.db import models

# Create your models here.

class Drivers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Vehicles(models.Model):
    id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey('Drivers',null=True, on_delete=models.SET_NULL)
    make = models.CharField(max_length = 300)
    model = models.CharField(max_length = 300)
    plate_number = models.CharField(max_length = 15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()