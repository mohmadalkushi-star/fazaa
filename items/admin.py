from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display  = ['name', 'owner', 'category', 'price', 'is_free', 'is_available', 'neighborhood']
    list_filter   = ['category', 'condition', 'is_free', 'is_available']
    search_fields = ['name', 'neighborhood']