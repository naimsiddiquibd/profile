from django.db import models

# Create your models here.


class txtmessages(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=750)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'A. Check Emails'
        verbose_name_plural = 'A. Check Emails'
