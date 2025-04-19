from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request/<int:item_id>/', views.request_item, name='request_item'),

    # Admin-only request management
    path('admin/requests/', views.view_requests, name='view_requests'),
    path('admin/requests/approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('admin/requests/reject/<int:request_id>/', views.reject_request, name='reject_request'),
]
