from django.contrib import admin
from .models import Destination, Review
# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'price', 'rating')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
