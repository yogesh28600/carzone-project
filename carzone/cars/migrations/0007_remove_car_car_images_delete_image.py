# Generated by Django 5.0.1 on 2024-01-19 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_image_car_car_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_images',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
