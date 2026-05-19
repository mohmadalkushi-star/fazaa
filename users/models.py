from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user          = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone         = models.CharField(max_length=15)
    city          = models.CharField(max_length=100, default='ينبع')
    neighborhood  = models.CharField(max_length=100)
    avatar        = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_verified   = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.neighborhood}"