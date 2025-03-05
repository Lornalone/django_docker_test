from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "quantity", "category"]
    list_filter = ("category",)

admin.site.register(Category)
admin.site.register(Tag)
