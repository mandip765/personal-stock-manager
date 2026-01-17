from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_item, name='add_item'),
    path('scan/', views.upload_bill, name='upload_bill'),
]
