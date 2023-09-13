from django.db import models

# Create your models here.
class UserProfile(models.Model):
    zimage = models.ImageField(upload_to="user_images")
    # zimage = models.FileField(upload_to="user_images")
