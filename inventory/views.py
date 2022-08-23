from django.shortcuts import render
from inventory.models import Item
from django.http import HttpResponse
from inventory.forms import AddItemForm
from django.views import View
class ItemView(View):
    form_class=AddItemForm
    # initial={'key','value'}
    template_name='list.html' 
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponse('/success/')

        return render(request, self.template_name, {'form': form})

    # def list_items(request):

    #     items = Item.objects.all()
    #     context = {
    #         'items':items,
    #         'form':AddItemForm()
    #     }

    #     return render(request, template_name='list.html', context=context)

def add_item(request):

    return HttpResponse('ADd item here')