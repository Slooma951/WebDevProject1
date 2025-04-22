from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Coach', 'Coach'),
        ('Customer', 'Customer')
    ]


class Category(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    item_condition = models.CharField(max_length=10, choices=[('New', 'New'), ('Used', 'Used')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)
