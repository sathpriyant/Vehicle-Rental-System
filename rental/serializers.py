
from rest_framework import serializers
from rental.models import OwnerDB, VehicleDB, RentalDB


class OwnerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    location = serializers.CharField(max_length=100)


class VehicleSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=OwnerDB.objects.all()
    )
    vehicle_name = serializers.CharField(max_length=200)
    vehicle_number = serializers.CharField(max_length=50)
    vehicle_type = serializers.ChoiceField(
        choices=VehicleDB.VEHICLE_TYPE_CHOICES
    )
    rent_per_day = serializers.IntegerField()
    is_available = serializers.BooleanField(default=True)


class RentalSerializer(serializers.Serializer):
    vehicle = serializers.PrimaryKeyRelatedField(
        queryset=VehicleDB.objects.all()
    )
    customer_name = serializers.CharField(max_length=200)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    total_amount = serializers.IntegerField()
    status = serializers.CharField(max_length=50)
