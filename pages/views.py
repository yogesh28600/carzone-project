from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured = True)
    latest_cars = Car.objects.order_by('-created_date')[:3]
    models = Car.objects.values_list('model', flat=True).distinct()
    years = Car.objects.values_list('year', flat=True).distinct()
    cities = Car.objects.values_list('city', flat=True).distinct()
    conditions = Car.objects.values_list('condition', flat=True).distinct()
    body_styles = Car.objects.values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()
    data = {
        'teams' : teams,
        'featured_cars':featured_cars,
        'latest_cars':latest_cars,
        'models':models,
        'years':years,
        'cities':cities,
        'conditions':conditions,
        'body_styles':body_styles,
        'transmissions':transmissions,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            send_mail(
                subject,
                message +'  Contact: '+ phone + 'Name:' + name,
                'settings.EMAIL_HOST_USER',
                [email],
                fail_silently=False,
            )
            messages.success(request,'Email was sent successfully')
        except:
            messages.error(request,'Email not sent, please re-try')

    return render(request,'pages/contact.html')