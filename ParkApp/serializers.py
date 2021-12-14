from django.db import models
from rest_framework import serializers
from ParkApp.models import Drivers, Vehicles

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drivers
        fields=('id', 'first_name', 'last_name', 'created_at', 'updated_at')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicles
        fields=('id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at')