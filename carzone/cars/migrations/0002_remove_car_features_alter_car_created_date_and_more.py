# Generated by Django 5.0.1 on 2024-01-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Disel', 'Disel'), ('CNG', 'CNG'), ('Electric', 'Electric')], max_length=50),
        ),
    ]
