from django.db import models

# Create your models here.


class basicpack(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=250)
    message = models.TextField(max_length=750)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'A. Basic Pack'
        verbose_name_plural = 'A. Basic Pack'


class standardpack(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=250)
    message = models.TextField(max_length=750)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'B. Standard Pack'
        verbose_name_plural = 'B. Standard Pack'


class propack(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    number = models.CharField(max_length=250)
    message = models.TextField(max_length=750)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'C. Premium Pack'
        verbose_name_plural = 'C. Premium Pack'
