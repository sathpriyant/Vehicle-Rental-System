from django.db import models

# Create your models here.


class OwnerDB(models.Model):
    owner_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.owner_name


class VehicleDB(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ("car", "Car"),
        ("bike", "Bike"),
        ("scooter", "Scooter"),
    )

    owner = models.ForeignKey(
        OwnerDB,
        on_delete=models.CASCADE,
        related_name="vehicles"
    )
    vehicle_name = models.CharField(max_length=200)
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPE_CHOICES
    )
    rent_per_day = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_name


class RentalDB(models.Model):
    vehicle = models.ForeignKey(
        VehicleDB,
        on_delete=models.CASCADE,
        related_name="rentals"
    )
    customer_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name
