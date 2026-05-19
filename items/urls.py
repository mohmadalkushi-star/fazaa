from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('item/<int:pk>/', views.item_detail, name='item-detail'),
    path('add/', views.add_item, name='add-item'),
]