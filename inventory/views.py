from django.shortcuts import render
from inventory.models import Item
from django.http import HttpResponse
from inventory.forms import AddItemForm
@
def list_items(request):

    items = Item.objects.all()
    context = {
        'items':items,
        'form':AddItemForm()
    }

    return render(request, template_name='list.html', context=context)

def add_item(request):

    return HttpResponse('ADd item here')