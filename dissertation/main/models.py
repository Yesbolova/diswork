from django.db import models
from django import forms

class aigerim (models.Model):
    title = models.CharField (max_length=255)
    image = models.ImageField("фотография", upload_to="kartinki/images", default = "", blank=True)


    def __str__(self):
        return self.title




