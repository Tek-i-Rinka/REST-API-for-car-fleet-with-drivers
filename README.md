# REST API for car fleet with drivers

### developed query processing for two tables

##### There is two tables:

    Driver:
    + id: int
    + first_name: str
    + last_name: str
    + created_at
    + updated_at

    Vehicle
    + id: int
    + driver_id: FK to Driver
    + make: str
    + model: str
    + plate_number: str  - format example "AA 1234 OO"
    + created_at
    + updated_at

##### The API processes the following requests:

    Driver:
    + GET /drivers/driver/ - output of the list of drivers
    + GET /drivers/driver/?created_at__gte={10-11-2021} - output of the list of drivers created after 10-11-2021
    + GET /drivers/driver/?created_at__lte={16-11-2021} - output of the list of drivers created before 16-11-2021

    + GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
    + POST /drivers/driver/ - creating a new driver
    + UPDATE /drivers/driver/<driver_id>/ - driver editing
    + DELETE /drivers/driver/<driver_id>/ - driver removal

    Vehicle:
    + GET /vehicles/vehicle/ - output of the list of machines
    + GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
    + GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers

    + GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific machine
    + POST /vehicles/vehicle/ - creating a new machine
    + UPDATE /vehicles/vehicle/<vehicle_id>/ - machine editing
    + POST /vehicles/set_driver/<vehicle_id>/?driver_id={4} - put the driver with id 4 in the car
    + POST /vehicles/set_driver/<vehicle_id>/ - get the driver out of the car
    + DELETE /vehicles/vehicle/<vehicle_id>/ - removing the machine
