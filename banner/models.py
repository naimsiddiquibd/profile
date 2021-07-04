from django.db import models

# Create your models here.
class banner(models.Model):
    headline = models.CharField(max_length=150)
    title1 = models.CharField(max_length=150)
    title2 = models.CharField(max_length=150)
    title3 = models.CharField(max_length=150)
    

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'A. Headline and Titles'
        verbose_name_plural = 'A. Headline and Titles'

class sm(models.Model):
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'B. Social Media Link'
        verbose_name_plural = 'B. Social Media Link'

class hireme(models.Model):
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'C. Button'
        verbose_name_plural = 'C. Button'