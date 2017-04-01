# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_censusblock_censushousehold65plus_fcbproportion_fmashapes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FMAStats',
            fields=[
                ('fma', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('fma_population_total', models.IntegerField(blank=True, null=True)),
                ('percent_owner_occ_hh', models.FloatField(blank=True, null=True)),
                ('percent_renter_occ_hh', models.FloatField(blank=True, null=True)),
                ('median_hh_income', models.IntegerField(blank=True, null=True)),
                ('percent_w_hinsurance', models.FloatField(blank=True, null=True)),
                ('percent_wo_hinsurance', models.FloatField(blank=True, null=True)),
                ('percent_college_grad_or_higher', models.FloatField(blank=True, null=True)),
                ('percent_rec_fs', models.FloatField(blank=True, null=True)),
                ('percent_total_lesh', models.FloatField(blank=True, null=True)),
                ('percent_non_white', models.FloatField(blank=True, null=True)),
                ('percent_below_pov', models.FloatField(blank=True, null=True)),
                ('percent_member_65plus', models.FloatField(blank=True, null=True)),
                ('percent_diff_area', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'fma_api_rollup',
            },
        ),
        migrations.CreateModel(
            name='IncidentTimes',
            fields=[
                ('inctimes_id', models.IntegerField(primary_key=True, serialize=False)),
                ('incident_id', models.IntegerField(blank=True, null=True)),
                ('responder_id', models.IntegerField(blank=True, null=True)),
                ('realtime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'inctimes',
            },
        ),
        migrations.AlterModelTable(
            name='fma',
            table='fma_shapes',
        ),
    ]