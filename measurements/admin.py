from django.contrib import admin
from .models import Measurement, Shirt


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    fields = ('name', 'info', 'amount_charged', 'amount_paid', 'balance',)
    readonly_fields = ('balance',)


@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    fields = ('name', 'info', 'measurement', 'quantity', 'length',
              'half_length', 'shoulder', 'bust', 'underbust_waist',
              'waist', 'hip', 'round_sleeve_short', 'round_sleeve_long',
              'sleeve_length')
    readonly_fields = ('style_tag', 'material_sample_tag',)
