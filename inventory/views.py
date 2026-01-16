from django.shortcuts import render, redirect
from django.db.models import F
from .models import Item
from .forms import ItemForm

def dashboard(request):
    items = Item.objects.all()
    low = items.filter(quantity__lte=F('low_stock'))
    return render(request, 'inventory/dashboard.html', {'items': items, 'low': low})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})
