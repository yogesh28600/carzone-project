# Generated by Django 5.0.1 on 2024-01-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_alter_inquiry_car_id_alter_inquiry_topic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
