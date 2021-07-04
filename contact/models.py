from django.db import models

# Create your models here.


class conthead(models.Model):
    headline = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=550)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'A. Headline, Title & Dscription'
        verbose_name_plural = 'A. Headline, Title & Dscription'
