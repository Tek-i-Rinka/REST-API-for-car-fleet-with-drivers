# SETUP

##### - download the archive with my project and unzip it

##### - open cmd and use these commands:

     pip install django
     pip install djangorestframework
     pip install django-cors-headers

##### - then open folder with my project and open cmd here (right-click->"open with windows terminal") use these command:

     python manage.py runserver

##### - copy url

##### - I used Postman for test requests(you can use your soft). To download Postman - https://www.postman.com/downloads/

##### - paste request URL

##### The API processes the following requests:

    Driver:
    + GET {url}/drivers/driver/ - output of the list of drivers
    + GET {url}/drivers/driver/?created_at__gte={10-11-2021} - output of the list of drivers created after 10-11-2021
    + GET {url}/drivers/driver/?created_at__lte={16-11-2021} - output of the list of drivers created before 16-11-2021

    + GET {url}/drivers/driver/<driver_id>/ - obtaining information on a particular driver
    + POST {url}/drivers/driver/ - creating a new driver
    + UPDATE {url}/drivers/driver/<driver_id>/ - driver editing
    + DELETE {url}/drivers/driver/<driver_id>/ - driver removal

    Vehicle:
    + GET {url}/vehicles/vehicle/ - output of the list of machines
    + GET {url}/vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
    + GET {url}/vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers

    + GET {url}/vehicles/vehicle/<vehicle_id> - obtaining information on a specific machine
    + POST {url}/vehicles/vehicle/ - creating a new machine
    + UPDATE {url}/vehicles/vehicle/<vehicle_id>/ - machine editing
    + POST {url}/vehicles/set_driver/<vehicle_id>/?driver_id={4} - put the driver with id 4 in the car
    + POST {url}/vehicles/set_driver/<vehicle_id>/ - get the driver out of the car
    + DELETE {url}/vehicles/vehicle/<vehicle_id>/ - removing the machine
