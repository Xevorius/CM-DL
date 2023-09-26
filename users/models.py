from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img_width, img_height = img.size
            size = min(img.size)
            cropped_img = img.crop(((img_width - size) // 2,
                                 (img_height - size) // 2,
                                 (img_width + size) // 2,
                                 (img_height + size) // 2))
            output_size = (300, 300)
            cropped_img.thumbnail(output_size)
            cropped_img.save(self.image.path)

