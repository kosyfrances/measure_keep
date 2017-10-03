from django.db import models
from django.utils.html import mark_safe


class Base(models.Model):

    info = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Measurement(Base):

    name = models.CharField(max_length=250)
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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.balance = self.amount_charged - self.amount_paid
        return super().save(*args, **kwargs)


class CommonComputation(Base):

    name = models.CharField(max_length=250, blank=True)
    measurement = models.ForeignKey(Measurement)
    quantity = models.PositiveIntegerField(default=1)
    length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    waist = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    hip = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = "{}'s shirt".format(self.measurement.name)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ImageUpload(models.Model):

    style = models.ImageField(upload_to='style/', blank=True)
    material_sample = models.ImageField(upload_to='sample/', blank=True)

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

    class Meta:
        abstract = True


class AbstractShirt(CommonComputation, ImageUpload):

    shoulder = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    half_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    bust = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    underbust_waist = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    sleeve_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    round_sleeve_short = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    round_sleeve_long = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    class Meta:
        abstract = True


class AbstractBlouse(AbstractShirt):

    nipple_to_nipple = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    shoulder_to_nipple = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    underbust_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    class Meta:
        abstract = True


class Shirt(AbstractShirt):

    def __str__(self):
        return self.name


class Blouse(AbstractBlouse):

    def __str__(self):
        return self.name


class Gown(AbstractBlouse):

    def __str__(self):
        return self.name


class Trouser(CommonComputation, ImageUpload):

    flap = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    down = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    lap = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return self.name


class Skirt(CommonComputation, ImageUpload):

    half_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return self.name
