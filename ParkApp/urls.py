from django.urls import path, re_path
from ParkApp import views


urlpatterns=[
    path('drivers/driver/', views.driverApi),
    path('vehicles/vehicle/', views.vehicleApi),
    path('drivers/driver/<int:id>/', views.driverApi),
    path('vehicles/vehicle/<int:id>/', views.vehicleApi),
    path('vehicles/set_driver/<int:id>/', views.vehicleApi),
]