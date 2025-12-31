from django.shortcuts import render, get_object_or_404
from .models import Apartment

def homepage(request):
    apartments = Apartment.objects.all()
    return render(request, 'listings/homepage.html', {'apartments': apartments})

def detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'listings/detaily_bytu.html', {'apartment': apartment})