from django.shortcuts import render
from .models import Car
# Create your views here.
def cars_home(request):
    cars = Car.objects.all()
    data = {
        'cars':cars
    }
    return render(request,'cars/cars_home.html',data)