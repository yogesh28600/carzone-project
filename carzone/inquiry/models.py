from django.db import models
from cars.models import Car
from django.contrib.auth.models import User
# Create your models here.
class Inquiry(models.Model):
    #Feilds
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True,null=True)
    comment = models.TextField(max_length=1000,blank=True,null=True)
    car_id = models.IntegerField()
    user_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add = True,null=True)

    def __str__(self):
        return self.email
