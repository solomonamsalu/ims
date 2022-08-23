from django.shortcuts import render
from inventory.models import Item
from django.http import HttpResponse
from inventory.forms import AddItemForm
from django.views import View
class ItemView(View):
    form_class=AddItemForm
    # initial={'key','value'}
    template_name='add_item.html' 
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

# class ListItemView(View):

#     def get(request, *args, **kwargs):

#         items = Item.objects.all()
#         context = {
#             'items': items
#         }
#         return render(request, 'list.html', context)


from django.views.generic.list import ListView
   
class ListItemView(ListView):
   
    # specify the model for list view
    model = Item
    template_name = 'list.html'
    queryset = Item.objects.all()
   
   