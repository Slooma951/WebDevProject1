from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('request/<int:item_id>/', views.request_item, name='request_item'),
]
