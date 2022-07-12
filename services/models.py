from distutils.command.upload import upload
from django.db import models

# Create your models here.

TRANSLATE_TO = (
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("af", "Twi"),
    ("ha", "Hausa"),
)

class ScanedTextImage(models.Model):
    image = models.ImageField(upload_to="scanned_images/")
    scanned_text = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


class TranslateText(models.Model):
    text = models.TextField()
    translate_to = models.CharField(choices=TRANSLATE_TO, max_length=100, null=True,blank=True)
    translated_text = models.TextField(null=True,blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class TextToSpeech(models.Model):
    text = models.TextField()
    audio_file = models.FileField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text