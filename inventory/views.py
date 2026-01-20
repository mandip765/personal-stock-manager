from django.shortcuts import render, redirect
from django.db.models import F
from .models import Item
from .ocr import read_bill

def dashboard(request):
    items = Item.objects.all()
    low = Item.objects.filter(quantity__lte=F('low_stock'))
    return render(request,'inventory/dashboard.html',{
        'items':items,'low':low
    })

def add_item(request):
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            low_stock=request.POST['low_stock']
        )
        return redirect('/')
    return render(request,'inventory/add_item.html')

def upload_bill(request):
    if request.method == 'POST':
        file = request.FILES['bill']
        with open('bill.jpg','wb+') as f:
            for c in file.chunks():
                f.write(c)
        text = read_bill('bill.jpg')
        return render(request,'inventory/upload_bill.html',{'text':text})
    return render(request,'inventory/upload_bill.html')
