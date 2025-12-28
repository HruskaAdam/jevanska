from django.shortcuts import render
from .models import Apartment 

def homepage(request):
    apartments = Apartment.objects.all()
    return render(request, 'listings/homepage.html', {'apartments': apartments})