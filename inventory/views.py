# Importing what we need
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Item, Request, Category

# Home view - shows items and category filter
@login_required
def home(request):
    request.user.refresh_from_db()  # makes sure the role updates if changed
    categories = Category.objects.all()
    selected = request.GET.get('category')

    if selected and selected.isdigit():
        items = Item.objects.filter(category__id=int(selected))  # filter items by category
        selected = int(selected)
    else:
        items = Item.objects.all()
        selected = None

    return render(request, 'inventory/home.html', {
        'items': items,
        'categories': categories,
        'selected': selected
    })

# Customer can request an item
@login_required
def request_item(request, item_id):
    item = Item.objects.get(id=item_id)
    Request.objects.create(user=request.user, item=item)
    return redirect('home')

# Check if user is admin
def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'

# Check if user is coach
def is_coach(user):
    return user.is_authenticated and user.role == 'Coach'

# Admin can view all requests
@user_passes_test(is_admin)
def view_requests(request):
    all_requests = Request.objects.select_related('user', 'item').all()
    return render(request, 'inventory/view_requests.html', {'requests': all_requests})

# Coach can see pending requests
@user_passes_test(is_coach)
def coach_approve_requests(request):
    player_requests = Request.objects.select_related('user', 'item').filter(status='Pending')
    return render(request, 'inventory/coach_requests.html', {'requests': player_requests})

# Users can see their own requests
@login_required
def my_requests(request):
    my_reqs = Request.objects.filter(user=request.user).select_related('item')
    return render(request, 'inventory/my_requests.html', {'requests': my_reqs})

# Admin or Coach can approve requests
@user_passes_test(lambda u: u.is_authenticated and u.role in ['Admin', 'Coach'])
def approve_request(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = 'Approved'
    req.save()
    return redirect('coach_requests' if request.user.role == 'Coach' else 'view_requests')

# Admin or Coach can reject requests
@user_passes_test(lambda u: u.is_authenticated and u.role in ['Admin', 'Coach'])
def reject_request(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = 'Rejected'
    req.save()
    return redirect('coach_requests' if request.user.role == 'Coach' else 'view_requests')
