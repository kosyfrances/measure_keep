from django.db import models
from django.utils.html import mark_safe


class Measurement(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField(blank=True, null=True)
    style = models.ImageField(upload_to='style/', blank=True)
    material_sample = models.ImageField(upload_to='sample/', blank=True)
    amount_charged = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00,
        editable=False, null=True
    )

    def style_tag(self):
        return mark_safe(
            '<a href="{}" target="_blank">'
            '<img src="{}" width="150" height="150"/>'
            '</a>'.format(
                self.style.url, self.style.url
            )
        )

    def material_sample_tag(self):
        return mark_safe(
            '<a href="{}" target="_blank">'
            '<img src="{}" width="150" height="150"/>'
            '</a>'.format(
                self.material_sample.url, self.material_sample.url
            )
        )

    material_sample_tag.short_description = 'Material sample image'
    style_tag.short_description = 'Style image'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.balance = self.amount_charged - self.amount_paid
        return super().save(*args, **kwargs)
