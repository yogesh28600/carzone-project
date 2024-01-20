from django.urls import path
from . import views
urlpatterns = [
    path('',views.cars_home,name='cars_home'),
    path('<int:id>',views.car_details,name='car_details'),
    path('search/',views.search,name='search'),
]