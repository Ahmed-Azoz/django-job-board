from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=15)
    image = models.models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)