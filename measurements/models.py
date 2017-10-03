from django.db import models


class Measurement(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()
    style = models.ImageField(upload_to='style/', blank=True)
    material_sample = models.ImageField(upload_to='sample/', blank=True)
    amount_charged = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return self.name
