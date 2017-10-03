from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Measurement, Shirt, Blouse, Gown, Trouser, Skirt


class Base(admin.ModelAdmin):
    readonly_fields = ('style_tag', 'material_sample_tag',)


class SharedBlouse(Base):
    fields = ('name', 'info', 'measurement', 'quantity', 'length',
              'half_length', 'underbust_length', 'shoulder', 'bust',
              'underbust_waist', 'waist', 'hip', 'round_sleeve_short',
              'round_sleeve_long', 'sleeve_length', 'nipple_to_nipple',
              'shoulder_to_nipple', 'style', 'style_tag', 'material_sample',
              'material_sample_tag',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    fields = ('name', 'info', 'amount_charged', 'amount_paid', 'balance',)
    readonly_fields = ('balance',)


@admin.register(Shirt)
class ShirtAdmin(Base):
    fields = ('name', 'info', 'measurement', 'quantity', 'length',
              'half_length', 'shoulder', 'bust', 'underbust_waist',
              'waist', 'hip', 'round_sleeve_short', 'round_sleeve_long',
              'sleeve_length', 'style', 'style_tag', 'material_sample',
              'material_sample_tag',)


@admin.register(Blouse)
class BlouseAdmin(SharedBlouse):
    pass


@admin.register(Gown)
class GownAdmin(SharedBlouse):
    pass


@admin.register(Trouser)
class TrouserAdmin(Base):
    fields = ('name', 'info', 'measurement', 'quantity', 'length', 'waist',
              'hip', 'flap', 'down', 'lap', 'style', 'style_tag',
              'material_sample', 'material_sample_tag',)


@admin.register(Skirt)
class SkirtAdmin(Base):
    fields = ('name', 'info', 'measurement', 'quantity', 'length', 'waist',
              'hip', 'half_length', 'style', 'style_tag', 'material_sample',
              'material_sample_tag',)


admin.site.unregister(Group)
