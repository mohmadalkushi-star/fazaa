from django.urls import path
from . import views

urlpatterns = [
    path('request/<int:item_pk>/', views.send_request, name='send-request'),
    path('dashboard/',             views.dashboard,    name='dashboard'),
    path('request/<int:request_pk>/<str:action>/', views.update_request_status, name='update-request'),
    path('review/<int:rental_pk>/', views.add_review, name='add-review'),
]