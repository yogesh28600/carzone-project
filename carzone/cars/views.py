from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars_home(request):
    cars = Car.objects.all()
    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars':paged_cars
    }
    return render(request,'cars/cars_home.html',data)