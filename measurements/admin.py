from django.contrib import admin
from .models import Measurement


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    fields = ('name', 'info', 'style', 'style_tag', 'material_sample',
              'material_sample_tag', 'amount_charged', 'amount_paid',
              'balance')
    readonly_fields = ('balance', 'style_tag', 'material_sample_tag',)
