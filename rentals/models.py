from django.db import models
from django.contrib.auth.models import User
from items.models import Item

class RentalRequest(models.Model):

    STATUS_CHOICES = [
        ('pending',  'بانتظار الموافقة'),
        ('accepted', 'مقبول'),
        ('rejected', 'مرفوض'),
        ('returned', 'تم الإرجاع'),
    ]

    borrower    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_requests')
    item        = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rental_requests')
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    start_date  = models.DateField()
    end_date    = models.DateField()
    message     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.borrower.username} ← {self.item.name}"


class Review(models.Model):

    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    rental      = models.OneToOneField(RentalRequest, on_delete=models.CASCADE, related_name='review')
    reviewer    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_reviews')
    rating      = models.IntegerField(choices=RATING_CHOICES)
    comment     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} - {self.rating} نجوم"