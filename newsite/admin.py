from django.contrib import admin

# Register your models here.

from .models import Attraction, Review

admin.site.register(Attraction)
admin.site.register(Review)