from distutils.command.upload import upload
from django.db import models

# Create your models here.
class ScanedTextImage(models.Model):
    image = models.ImageField(upload_to="scanned_images/")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)