from django.contrib import admin
from listings.models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'disposition', 'price', 'is_available')