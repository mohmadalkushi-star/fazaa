from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):

    # ─── التصنيفات المتاحة ───
    CATEGORY_CHOICES = [
        ('electric',  'كهربائية'),
        ('manual',    'يدوية'),
        ('outdoor',   'برية / رحلات'),
        ('other',     'أخرى'),
    ]

    # ─── حالة الأداة ───
    CONDITION_CHOICES = [
        ('excellent', 'ممتازة'),
        ('good',      'جيدة'),
        ('fair',      'مقبولة'),
    ]

    # ─── الحقول ───
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name        = models.CharField(max_length=100)
    description = models.TextField()
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    condition   = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price       = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_free     = models.BooleanField(default=False)
    image       = models.ImageField(upload_to='items/', blank=True, null=True)
    city         = models.CharField(max_length=100, default='')
    neighborhood = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name