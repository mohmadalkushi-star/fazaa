from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display  = ['user', 'phone', 'neighborhood', 'is_verified']
    list_filter   = ['is_verified', 'neighborhood']
    search_fields = ['user__username', 'phone']