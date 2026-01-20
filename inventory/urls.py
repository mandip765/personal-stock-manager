from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add/', views.add_item),
    path('bill/', views.upload_bill),
]
