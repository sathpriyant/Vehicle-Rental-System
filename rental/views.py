from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rental.models import OwnerDB, VehicleDB, RentalDB
from rental.serializers import OwnerSerializer, VehicleSerializer, RentalSerializer


class OwnerListCreateView(APIView):

    def get(self, request):
        qs = OwnerDB.objects.all()
        serializer_instance = OwnerSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = OwnerSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            OwnerDB.objects.create(**actual_data)
            return Response(data={"message": "owner added successfully"})
        else:
            return Response(data={"message": "Invalid data"})


class OwnerRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(OwnerDB, id=pk)
        serializer_instance = OwnerSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = OwnerSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            OwnerDB.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "owner updated successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        OwnerDB.objects.filter(id=pk).delete()
        return Response({"message": "owner deleted"})


class VehicleListCreateView(APIView):

    def get(self, request):
        qs = VehicleDB.objects.all()
        serializer_instance = VehicleSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = VehicleSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            VehicleDB.objects.create(**actual_data)
            return Response(data={"message": "vehicle added successfully"})
        else:
            return Response(data={"message": "Invalid data"})


class VehicleRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(VehicleDB, id=pk)
        serializer_instance = VehicleSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = VehicleSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            VehicleDB.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "vehicle updated successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(VehicleDB, id=pk)
        qs.delete()
        return Response(data={"message": "vehicle deleted successfully"})


class RentalListCreateView(APIView):

    def get(self, request):
        qs = RentalDB.objects.all()
        serializer_instance = RentalSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = RentalSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            RentalDB.objects.create(**actual_data)
            return Response(data={"message": "rental added successfully"})
        else:
            return Response(data={"message": "Invalid data"})


class RentalRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(RentalDB, id=pk)
        serializer_instance = RentalSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = RentalSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            RentalDB.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message": "rental updated successfully"})
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        qs = get_object_or_404(RentalDB, id=pk)
        qs.delete()
        return Response(data={"message": "rental deleted successfully"})


class OwnerWithVehiclesView(APIView):

    def get(self, request, pk):
        owner = get_object_or_404(OwnerDB, id=pk)
        vehicles = VehicleDB.objects.filter(owner_id=pk)

        owner_serializer = OwnerSerializer(owner)
        vehicle_serializer = VehicleSerializer(vehicles, many=True)

        data = {
            "owner": owner_serializer.data,
            "vehicles": vehicle_serializer.data
        }
        return Response(data=data)


class VehicleWithRentalsView(APIView):

    def get(self, request, pk):
        vehicle = get_object_or_404(VehicleDB, id=pk)
        rentals = RentalDB.objects.filter(vehicle_id=pk)

        vehicle_serializer = VehicleSerializer(vehicle)
        rental_serializer = RentalSerializer(rentals, many=True)

        data = {
            "vehicle": vehicle_serializer.data,
            "rentals": rental_serializer.data
        }
        return Response(data=data)
