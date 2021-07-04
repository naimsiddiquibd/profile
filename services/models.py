from django.db import models

# Create your models here.


class services(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A. Title & Subtitle'
        verbose_name_plural = 'A. Title & Subtitle'


class items(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    image = models.FileField(upload_to='services/')
    color = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Items'
        verbose_name_plural = 'B. Items'
