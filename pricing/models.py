from django.db import models

# Create your models here.


class pricehead(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A. Edit Title'
        verbose_name_plural = 'A. Edit Title'


class pricetable(models.Model):
    icon = models.FileField(upload_to='prices/')
    title = models.CharField(max_length=150)
    offer1 = models.CharField(max_length=150, blank=True)
    offer2 = models.CharField(max_length=150, blank=True)
    offer3 = models.CharField(max_length=150, blank=True)
    offer4 = models.CharField(max_length=150, blank=True)
    offer5 = models.CharField(max_length=150, blank=True)
    price = models.CharField(max_length=150)
    button = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Pricing Table'
        verbose_name_plural = 'B. Pricing Table'
