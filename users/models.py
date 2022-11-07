from django.db import models
from django.contrib.auth.models import User

from utils.image_utils import reduce_image_resolution


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # reduce image resolution if necessary
        reduce_image_resolution(self.image.path)
