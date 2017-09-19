from django.db import models


class Measurement(models.Model):
    name = models.CharField(max_length=250)
    style = models.ImageField(upload_to='', blank=True)
    material_sample = models.ImageField(upload_to='', blank=True)
    amount_charged = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
