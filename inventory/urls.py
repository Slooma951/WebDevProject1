from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('request/<int:item_id>/', views.request_item, name='request_item'),  # request item

    # Coach view pending requests
    path('coach/requests/', views.coach_approve_requests, name='coach_requests'),  # coach approves requests

    # Approvals - coach and admin both use this
    path('approve-request/<int:request_id>/', views.approve_request, name='approve_request'),  # approve request
    path('reject-request/<int:request_id>/', views.reject_request, name='reject_request'),  # reject request

    # Admin view of all requests
    path('admin/requests/', views.view_requests, name='view_requests'),  # admin view
]
