from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Item

# Create your views here.
def item_list(request):
    item_list = Item.objects.all() #get all the items
    paginator = Paginator(item_list,5) # It shows 5 items per page

    page_num = request.GET.get('page') #Get the page number from query string
    page_obj = paginator.get_page(page_num)

    context = {
        'page_obj':page_obj
    }

    return render(request,'item_list.html',context)
    