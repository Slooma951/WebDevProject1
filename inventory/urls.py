from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('request/<int:item_id>/', views.request_item, name='request_item'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    # Admin-only request management
    path('admin/requests/', views.view_requests, name='view_requests'),
    path('admin/requests/approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('admin/requests/reject/<int:request_id>/', views.reject_request, name='reject_request'),
]
