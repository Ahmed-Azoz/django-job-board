from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.

def image_upload(instance, file_name):
    imagename, extension = file_name.split(".")
    return "prof/%s.%s"%(instance.id, extension)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City", verbose_name=("user_city"), on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to=image_upload, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class City(models.Model):
    name = models.name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


