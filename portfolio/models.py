from django.db import models

# Create your models here.


class porthead(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A. Edit Title'
        verbose_name_plural = 'A. Edit Title'


class itemsb(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    button = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    feature = models.FileField(upload_to='portfolio/')
    image = models.FileField(upload_to='portfolio')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'B. Add Items'
        verbose_name_plural = 'B. Add Items'
