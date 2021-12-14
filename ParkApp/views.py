from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ParkApp.models import Drivers, Vehicles
from ParkApp.serializers import DriverSerializer, VehicleSerializer

from datetime import datetime

# Create your views here.

@csrf_exempt
def driverApi(request, id=0):
    if request.method == 'GET':
        try:
            get_created_at__gte = request.GET.get('created_at__gte', None)
            get_created_at__lte = request.GET.get('created_at__lte', None)
            if id!=0:
                drivers = Drivers.objects.get(id = id)
                drivers_serializer=DriverSerializer(drivers)
            elif get_created_at__gte!=None:
                date = datetime.strptime(get_created_at__gte, "%d-%m-%Y")
                drivers = Drivers.objects.all().filter(created_at__date__gte=date.strftime("%Y-%m-%d"))
                drivers_serializer=DriverSerializer(drivers, many=True)
            elif get_created_at__lte!=None:
                date = datetime.strptime(get_created_at__lte, "%d-%m-%Y")
                drivers = Drivers.objects.all().filter(created_at__date__lte=date.strftime("%Y-%m-%d"))
                drivers_serializer=DriverSerializer(drivers, many=True)    
            else:
                drivers = Drivers.objects.all()
                drivers_serializer=DriverSerializer(drivers, many=True)
            
            return JsonResponse(drivers_serializer.data, safe=False)    
        except Exception as ex:
            print(ex)
            return JsonResponse("error", safe=False)
    elif request.method == 'POST':
        drivers_data = JSONParser().parse(request)
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        drivers_data['id'] = 1
        drivers_data['created_at'] = now
        drivers_data['updated_at'] = now
        drivers_serializer = DriverSerializer(data=drivers_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(drivers_serializer.errors, safe=False)
    elif request.method == 'PUT':
        if id!=0:
            drivers_data=JSONParser().parse(request)
            drivers = Drivers.objects.get(id=id)
            now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            drivers_data['updated_at'] = now
            drivers_data['created_at'] = DriverSerializer(drivers).data['created_at']
            drivers_serializer=DriverSerializer(drivers, data=drivers_data)
        else:
            drivers_data=JSONParser().parse(request)
            drivers = Drivers.objects.get(id=drivers_data['id'])
            now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            drivers_data['updated_at'] = now
            drivers_data['created_at'] = DriverSerializer(drivers).data['created_at']
            drivers_serializer=DriverSerializer(drivers, data=drivers_data)
        if drivers_serializer.is_valid():
            drivers_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(drivers_serializer.errors, safe=False)
    elif request.method == 'DELETE':
        try:
            drivers=Drivers.objects.get(id=id)
            drivers.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse("error", safe=False)


@csrf_exempt
def vehicleApi(request, id=0):
    if request.method == 'GET':
        try:
            get_with_drivers = request.GET.get('with_drivers', None)
            if id!=0:
                vehicles = Vehicles.objects.get(id = id)
                vehicles_serializer=VehicleSerializer(vehicles)
            elif get_with_drivers!=None:
                if get_with_drivers.lower()[0:3]=="yes":  # приходит строка С и в конце стоит нуль-терминатор \x00 
                    print("here")
                    vehicles = Vehicles.objects.all().filter(driver_id__isnull=False)
                else:
                    vehicles = Vehicles.objects.all().filter(driver_id__isnull=True)
                vehicles_serializer=VehicleSerializer(vehicles, many=True) 
            else:
                vehicles = Vehicles.objects.all()
                vehicles_serializer=VehicleSerializer(vehicles, many=True)
            
            return JsonResponse(vehicles_serializer.data, safe=False)    
        except Exception as ex:
            print(ex)
            returnString = "error: " + str(ex)
            return JsonResponse(returnString, safe=False)
    elif request.method == 'POST':
        try:
            vehicles_data=JSONParser().parse(request)
            now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            if id==0:
                vehicles_data['id'] = 1
                vehicles_data['created_at'] = now
                vehicles_data['updated_at'] = now
                vehicle_serializer = VehicleSerializer(data=vehicles_data)
                if vehicle_serializer.is_valid():
                    vehicle_serializer.save()
                    return JsonResponse("Added Successfully", safe=False)
                return JsonResponse(vehicle_serializer.errors, safe=False)
            else:
                vehicles = Vehicles.objects.get(id=id)
                vehicles_data['updated_at'] = now
                vehicles_data['created_at'] = VehicleSerializer(vehicles).data['created_at']
                vehicle_serializer=VehicleSerializer(vehicles, data=vehicles_data)
                get_driver_id = request.GET.get('driver_id', None)
                if get_driver_id != None:
                    vehicles_data['driver_id'] = int(get_driver_id)
                else:
                    vehicles_data['driver_id'] = None
                if vehicle_serializer.is_valid():
                    vehicle_serializer.save()
                    return JsonResponse("Driver ID Updated Successfully", safe=False)
                return JsonResponse(vehicle_serializer.errors, safe=False)      
        except Exception as ex:
            print(ex)
            returnString = "error: " + str(ex)
            return JsonResponse(returnString, safe=False)
    elif request.method == 'PUT':
        try:
            if id!=0:
                vehicles_data=JSONParser().parse(request)
                vehicles = Vehicles.objects.get(id=id)
                now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                vehicles_data['updated_at'] = now
                vehicles_data['created_at'] = VehicleSerializer(vehicles).data['created_at']
                vehicles_serializer=VehicleSerializer(vehicles, data=vehicles_data)
            else:
                vehicles_data=JSONParser().parse(request)
                vehicles = Vehicles.objects.get(id=vehicles_data['id'])
                now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                vehicles_data['updated_at'] = now
                vehicles_data['created_at'] = DriverSerializer(vehicles).data['created_at']
                vehicles_serializer=VehicleSerializer(vehicles, data=vehicles_data)
            if vehicles_serializer.is_valid():
                vehicles_serializer.save()
                return JsonResponse("Update Successfully", safe=False)
            return JsonResponse(vehicles_serializer.errors, safe=False)
        except Exception as ex:
            print(ex)
            returnString = "error: " + str(ex)
            return JsonResponse(returnString, safe=False)
    elif request.method == 'DELETE':
        try:
            vehicles=Vehicles.objects.get(id=id)
            vehicles.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Exception as ex:
            print(ex)
            returnString = "error: " + str(ex)
            return JsonResponse(returnString, safe=False)
