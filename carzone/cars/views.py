from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars_home(request):
    cars = Car.objects.order_by('-created_date')

    models = Car.objects.values_list('model', flat=True).distinct()
    years = Car.objects.values_list('year', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    conditions = Car.objects.values_list('condition', flat=True).distinct()
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()

    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars':paged_cars,
        'models':models,
        'years':years,
        'cities':cities,
        'conditions':conditions,
        'body_styles':body_styles,
        'transmissions':transmissions,
    }
    return render(request,'cars/cars_home.html',data)
def car_details(request,id):
    car = get_object_or_404(Car,pk=id)
    data = {
        'car':car
    }
    return render(request,'cars/car_details.html',data)
def search(request):
    cars = Car.objects.order_by('-created_date')
    models = Car.objects.values_list('model', flat=True).distinct()
    years = Car.objects.values_list('year', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    conditions = Car.objects.values_list('condition', flat=True).distinct()
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET and request.GET['keyword'] != None:
        cars = cars.filter(description__icontains = request.GET['keyword'])
    if 'model' in request.GET and request.GET['model'] != None:
        cars = cars.filter(model__iexact = request.GET['model'])
    if 'year' in request.GET and request.GET['year'] != None:
        cars = cars.filter(year__iexact = request.GET['year'])
    if 'city' in request.GET and request.GET['city'] != None:
        cars = cars.filter(city__iexact = request.GET['city'])
    if 'condition' in request.GET and request.GET['condition'] != None:
        cars = cars.filter(conditionl__iexact = request.GET['condition'])
    if 'body_style' in request.GET and request.GET['body_style'] != None:
        cars = cars.filter(body_style__iexact = request.GET['body_style'])
    if 'transmission' in request.GET and request.GET['transmission'] != None:
        cars = cars.filter(transmission__iexact = request.GET['transmission'])
    if 'min_price' in request.GET:
        cars = cars.filter(price__gte = request.GET['min_price'],price__lte = request.GET['max_price'])
    data={
        'cars':cars,
        'models':models,
        'years':years,
        'cities':cities,
        'conditions':conditions,
        'body_styles':body_styles,
        'transmissions':transmissions,
    }
    return render(request,'cars/search.html',data)