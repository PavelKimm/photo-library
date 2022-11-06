from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
