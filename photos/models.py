from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from utils.image_utils import reduce_image_resolution


class Photo(models.Model):
    file = models.ImageField(upload_to='photos/')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.file} {self.caption}'.strip()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # reduce image resolution if necessary
        reduce_image_resolution(self.file.path, resolution_threshold=650)

    @staticmethod
    def get_absolute_url():
        # for redirect after creating new photo
        return reverse('home-page')
