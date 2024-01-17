from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display=('id','first_name','designation')
    list_display_links=('id','first_name')

admin.site.register(models.Team,TeamAdmin)
admin.site.unregister(Group)