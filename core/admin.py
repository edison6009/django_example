from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('description',)












