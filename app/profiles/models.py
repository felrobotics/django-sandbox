from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # commented to use Image Field
    # image_as_file = models.FileField(upload_to="images", null=True)
    # however django has also a specialiez field for images, let's use it

    image = models.ImageField(upload_to="images", null=True)
