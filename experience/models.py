from django.db import models

# Create your models here.


class experience(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A. Title'
        verbose_name_plural = 'A. Title'


class education(models.Model):
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Add Education'
        verbose_name_plural = 'B. Add Education'


class workhis(models.Model):
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Add Experience'
        verbose_name_plural = 'B. Add Experience'
