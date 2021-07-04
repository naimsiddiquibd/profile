from django.db import models

# Create your models here.


class about(models.Model):
    headline = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    button = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    image = models.FileField(upload_to='profile/')

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'A. Headline, Description & Image'
        verbose_name_plural = 'A. Headline, Description & Image'


class skills(models.Model):
    skill = models.CharField(max_length=150)
    rate = models.CharField(max_length=150)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'B. Skills'
        verbose_name_plural = 'B. Skills'

class counter(models.Model):
    value = models.CharField(max_length=150)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'D. Counter'
        verbose_name_plural = 'D. Counter'
