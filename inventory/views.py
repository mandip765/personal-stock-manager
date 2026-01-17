from django.shortcuts import render, redirect
from .models import Item
from .ocr import read_bill
from django.core.files.storage import default_storage

def dashboard(request):
    items = Item.objects.all()
    low = Item.objects.filter(quantity__lte=models.F('low_stock'))
    return render(request, 'inventory/dashboard.html', {
        'items': items,
        'low': low
    })

def add_item(request):
    if request.method == "POST":
        Item.objects.create(
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            low_stock=request.POST['low_stock']
        )
        return redirect('dashboard')
    return render(request, 'inventory/add_item.html')

def upload_bill(request):
    matched = []

    if request.method == "POST" and 'bill' in request.FILES:
        path = default_storage.save('bill.jpg', request.FILES['bill'])
        extracted = read_bill(default_storage.path(path))

        for e in extracted:
            for item in Item.objects.all():
                if item.name.lower() in e['name']:
                    matched.append({
                        "item": item,
                        "qty": e['qty'],
                        "unit": e['unit']
                    })

    if request.method == "POST" and 'confirm' in request.POST:
        for k, v in request.POST.items():
            if k.startswith("item_"):
                item = Item.objects.get(id=k.replace("item_", ""))
                item.quantity += int(v)
                item.save()
        return redirect('dashboard')

    return render(request, 'inventory/upload_bill.html', {'matched': matched})
