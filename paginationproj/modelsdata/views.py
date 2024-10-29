from django.shortcuts import render
from .models import ItemList

# Create your views here.
def item_data(request):
    items = ItemList.objects.all()
    return render(request,'items_data.html',{'items':items})