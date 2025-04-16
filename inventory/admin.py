from django.contrib import admin
from .models import User, Category, Item, Request, Log

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Request)
admin.site.register(Log)
