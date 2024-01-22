from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here. 
class Car(models.Model):
    # CHOICES
    fuel_type_choice = (
        ('Petrol','Petrol'),
        ('Disel','Disel'),
        ('CNG','CNG'),
        ('Electric','Electric'),
    )
    state_choice = (
        ("AN","Andaman and Nicobar Islands"),
        ("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CG","Chhattisgarh"),
        ("CH","Chandigarh"),
        ("DN","Dadra and Nagar Haveli"),
        ("DD","Daman and Diu"),
        ("DL","Delhi"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("LA","Ladakh"),
        ("LD","Lakshadweep"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OD","Odisha"),
        ("PB","Punjab"),
        ("PY","Pondicherry"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TS","Telangana"),
        ("TR","Tripura"),
        ("UP","Uttar Pradesh"),
        ("UK","Uttarakhand"),
        ("WB","West Bengal")
    )
    feature_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    year_choices =[]
    for i in range(2000,datetime.now().year+1):
        year_choices.append((i,i))
    sale_choices = (
        ('Rent','Rent'),
        ('Sale','Sale'),
    )
    body_style_choices = (
        ('Hatchback','Hatchback'),
        ('Sedan','Sedan'),
        ('MUV/SUV','MUV/SUV'),
        ('Coupe','Coupe'),
        ('Convertible','Convertible'),
        ('Wagon','Wagon'),
        ('Van','Van'),
        ('Jeep','Jeep'),
    )
    transmission_choices = (
        ('Manual','Manual'),
        ('Automatic','Automatic'),
        ('Semi-Automatic','Semi-Automatic'),
    )
    condition_choices = (
        ('Used','Used'),
        ('New','New'),
        ('Bad','Bad'),
    )
    
    #FEILDS
    car_title = models.CharField(max_length=255)
    sale = models.CharField(choices = sale_choices, default = 'Sale',max_length = 100)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choices)
    condition = models.CharField(choices=condition_choices,max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices = feature_choices,null=True,blank = True,max_length=10000, max_choices = 100)
    body_style = models.CharField(choices = body_style_choices,max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(choices = transmission_choices,max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.DecimalField(max_digits=20, decimal_places=2)
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    milage = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(choices=fuel_type_choice , max_length=50)
    no_of_owners = models.CharField(max_length=100)
    description = RichTextField(null = True, blank = True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_title