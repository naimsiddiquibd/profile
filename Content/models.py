from django.db import models

# Create your models here.


class Settings(models.Model):
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    favicon = models.FileField(upload_to='favicon/')
    preview = models.FileField(upload_to='preview/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A. Settings'
        verbose_name_plural = 'A. Settings'


class Logo(models.Model):
    title = models.CharField(max_length=150)
    logo = models.FileField(upload_to='logo/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Change Logo'
        verbose_name_plural = 'B. Change Logo'


class Menu(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'C. Menu'
        verbose_name_plural = 'C. Menu'
