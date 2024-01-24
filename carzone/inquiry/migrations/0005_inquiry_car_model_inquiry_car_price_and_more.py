# Generated by Django 5.0.1 on 2024-01-22 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0004_alter_inquiry_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='car_model',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='car_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='car_title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]