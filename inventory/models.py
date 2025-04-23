from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model with roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Coach', 'Coach'),
        ('Customer', 'Customer')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Customer')


# Category model for item grouping
class Category(models.Model):
    name = models.CharField(max_length=100)


# Item model for football gear
class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    item_condition = models.CharField(max_length=10, choices=[('New', 'New'), ('Used', 'Used')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# Request model for item requests by users
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)


# Log model to track actions
class Log(models.Model):
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)
