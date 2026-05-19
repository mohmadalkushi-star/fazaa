from django.contrib import admin
from .models import RentalRequest, Review

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display  = ['borrower', 'item', 'status', 'start_date', 'end_date']
    list_filter   = ['status']
    search_fields = ['borrower__username', 'item__name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ['reviewer', 'rental', 'rating']
    list_filter   = ['rating']