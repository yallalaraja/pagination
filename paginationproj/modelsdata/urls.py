from django.urls import path
from .views import item_data

urlpatterns = [
    path('item_list/',item_data,name='item_data')
]