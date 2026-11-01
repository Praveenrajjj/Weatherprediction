from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class UserPredictModel(models.Model):
    City = models.CharField(max_length=100)
    Temperature_Celsius = models.FloatField()
    Wind_Speed_ms = models.FloatField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Description = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)  # This will sto

    def __str__(self):
        return f"Prediction: {self.Description}"
    


