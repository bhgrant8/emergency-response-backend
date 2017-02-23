# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-23 07:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170223_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensusBlock',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('statefp', models.CharField(blank=True, max_length=2, null=True)),
                ('countyfp', models.CharField(blank=True, max_length=3, null=True)),
                ('tractce', models.CharField(blank=True, max_length=6, null=True)),
                ('blkgrpce', models.CharField(blank=True, max_length=1, null=True)),
                ('geoid', models.CharField(blank=True, max_length=12, null=True)),
                ('namelsad', models.CharField(blank=True, max_length=13, null=True)),
                ('mtfcc', models.CharField(blank=True, max_length=5, null=True)),
                ('funcstat', models.CharField(blank=True, max_length=1, null=True)),
                ('aland', models.FloatField(blank=True, null=True)),
                ('awater', models.FloatField(blank=True, null=True)),
                ('intptlat', models.CharField(blank=True, max_length=11, null=True)),
                ('intptlon', models.CharField(blank=True, max_length=12, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4269)),
            ],
            options={
                'db_table': 'ceblocks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CensusHousehold65Plus',
            fields=[
                ('id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('id2', models.CharField(max_length=12)),
                ('geography', models.CharField(max_length=60)),
                ('totals', models.IntegerField()),
                ('oneplus_people_65plus', models.IntegerField()),
                ('one_or_more_people_65plus_1_person', models.IntegerField()),
                ('oneplus_people_65plus_2plus_person', models.IntegerField()),
                ('oneplus_people_65plus_2plus_person_family', models.IntegerField()),
                ('oneplus_people_65plus_2plus_person_nonfamily', models.IntegerField()),
                ('no_people_65plus', models.IntegerField()),
                ('no_people_65plus_1_person', models.IntegerField()),
                ('no_people_65plus_2plus_person', models.IntegerField()),
                ('no_people_65plus_2plus_person_family', models.IntegerField()),
                ('no_people_65plus_2plus_person_nonfamily', models.IntegerField()),
            ],
            options={
                'db_table': 'census_households_65plus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FcbProportion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_block', models.CharField(blank=True, max_length=12, null=True)),
                ('fire_block', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('overlap_cbg', models.FloatField(blank=True, null=True)),
                ('overlap_fb', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fcb_proportion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FmaShapes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fma', models.CharField(blank=True, max_length=2, null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=0)),
            ],
            options={
                'db_table': 'fma_shapes',
                'managed': False,
            },
        ),
    ]
