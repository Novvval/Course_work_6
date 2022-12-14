from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)


class Comment(models.Model):
    text = models.CharField(max_length=8000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
