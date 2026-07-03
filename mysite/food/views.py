from django.shortcuts import render
from django.http import HttpResponse
from.models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'food/index.html', context)
def item(request):
    return HttpResponse("<h1>Hello, world. You're at the item page.")
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
