# Generated by Django 5.0.1 on 2024-01-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0003_inquiry_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]