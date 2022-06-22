from distutils.command.upload import upload
from django.db import models

# Create your models here.

TRANSLATE_TO = (
    ("Spanish", "Spanish"),
    ("French", "French"),
    ("German", "German"),
)

class ScanedTextImage(models.Model):
    image = models.ImageField(upload_to="scanned_images/")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


class TranslateText(models.Model):
    text = models.TextField()
    translate_to = models.CharField(choices=TRANSLATE_TO, max_length=100)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text