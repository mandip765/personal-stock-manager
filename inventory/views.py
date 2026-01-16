from django.shortcuts import render
from django.db.models import F
from .models import Item

def dashboard(request):
    items = Item.objects.all()
    low = items.filter(quantity__lte=F('low_stock'))
    return render(request, 'inventory/dashboard.html', {
        'items': items,
        'low': low
    })
