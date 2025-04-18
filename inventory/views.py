from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Request, Category

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'inventory/home.html', {'items': items})

@login_required
def request_item(request, item_id):
    item = Item.objects.get(id=item_id)
    Request.objects.create(user=request.user, item=item)
    return redirect('home')
