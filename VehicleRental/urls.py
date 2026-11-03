"""
URL configuration for VehicleRental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rental import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('owner/', views.OwnerListCreateView.as_view()),
    path('owner/<int:pk>/', views.OwnerRetrieveUpdateDeleteView.as_view()),

    path('vehicle/', views.VehicleListCreateView.as_view()),
    path('vehicle/<int:pk>/', views.VehicleRetrieveUpdateDeleteView.as_view()),

    path('rental/', views.RentalListCreateView.as_view()),
    path('rental/<int:pk>/', views.RentalRetrieveUpdateDeleteView.as_view()),

    path('owner/<int:pk>/vehicles/', views.OwnerWithVehiclesView.as_view()),
    path('vehicle/<int:pk>/rentals/', views.VehicleWithRentalsView.as_view()),
]
