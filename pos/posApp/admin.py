"""
Developed by MASA
All Rights Reserved.
"""

from django.contrib import admin
from posApp.models import Category, Products, Sales, salesItems

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
