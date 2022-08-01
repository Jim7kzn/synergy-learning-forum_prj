from django.db import models

# Create your models here.


class Checkbox(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)
