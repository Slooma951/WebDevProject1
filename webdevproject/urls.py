# Import necessary modules for admin and url handling
from django.contrib import admin
from django.urls import path, include
from inventory import views
from django.contrib.auth import views as auth_views  # import built-in auth views

# URL patterns for the entire project
urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel
    path('', include('inventory.urls')),  # include urls from the inventory app
    path('my-requests/', views.my_requests, name='my_requests'),  # customer and coach view their requests
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),  # login page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # logout with redirect to login
]
