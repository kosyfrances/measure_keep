# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('waist', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('hip', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('style', models.ImageField(blank=True, upload_to='style/')),
                ('material_sample', models.ImageField(blank=True, upload_to='sample/')),
                ('shoulder', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('half_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bust', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('underbust_waist', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sleeve_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('round_sleeve_short', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('round_sleeve_long', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('nipple_to_nipple', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('shoulder_to_nipple', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('underbust_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('amount_charged', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('waist', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('hip', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('style', models.ImageField(blank=True, upload_to='style/')),
                ('material_sample', models.ImageField(blank=True, upload_to='sample/')),
                ('shoulder', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('half_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bust', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('underbust_waist', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sleeve_length', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('round_sleeve_short', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('round_sleeve_long', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.Measurement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blouse',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.Measurement'),
        ),
    ]
