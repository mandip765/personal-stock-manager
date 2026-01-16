from django.shortcuts import render, redirect
from .models import Item

def dashboard(request):
    items = Item.objects.all()
    low = items.filter(quantity__lte=models.F('low_stock'))
    return render(request, 'inventory/dashboard.html', {'items': items, 'low': low})
