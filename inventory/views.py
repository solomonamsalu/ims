from django.shortcuts import render
from inventory.models import Item

def list_items(request):

    items = Item.objects.all()

    return render(request, template_name='list.html', context=items)