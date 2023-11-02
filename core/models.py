from django.db import models,migrations


# Create your models here.

class GeneralSettings(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )

    parameters = models.CharField(
        default='',
        blank=True,
        max_length=254,
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    update_date = models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    create_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
