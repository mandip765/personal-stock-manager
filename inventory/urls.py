from django.urls import path
from .views import dashboard, add_item

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_item, name='add_item'),
]
