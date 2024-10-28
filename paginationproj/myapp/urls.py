from django.urls import path
from .views import item_list

urlpatterns = [
    path('item/',item_list,name='item_list')
]