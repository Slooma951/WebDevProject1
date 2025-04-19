from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Item, Request, Category

#Home view — already working
@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'inventory/home.html', {'items': items})

#Request item view — already working
@login_required
def request_item(request, item_id):
    item = Item.objects.get(id=item_id)
    Request.objects.create(user=request.user, item=item)
    return redirect('home')

#Function to check if user is Admin
def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'

#View for Admin to see all item requests
@user_passes_test(is_admin)
def view_requests(request):
    all_requests = Request.objects.select_related('user', 'item').all()
    return render(request, 'inventory/view_requests.html', {'requests': all_requests})

#Approve a specific request (Admin only)
@user_passes_test(is_admin)
def approve_request(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = 'Approved'
    req.save()
    return redirect('view_requests')

#Reject a specific request (Admin only)
@user_passes_test(is_admin)
def reject_request(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = 'Rejected'
    req.save()
    return redirect('view_requests')
