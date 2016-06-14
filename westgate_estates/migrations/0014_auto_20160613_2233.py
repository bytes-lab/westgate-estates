# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-13 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0013_auto_20160613_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_search',
            name='cr_furnished',
            field=models.IntegerField(blank=True, choices=[(0, b'Furnished'), (1, b'Part Furnished'), (2, b'Unfurnished'), (3, b'Not Specified'), (4, b'Furnished/ Un Furnishedf')], null=True),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cr_high_bedroom',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cr_high_price',
            field=models.FloatField(default=99999),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cr_low_bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cr_low_price',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cs_high_bedroom',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cs_high_price',
            field=models.FloatField(default=99999),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cs_low_bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='save_search',
            name='cs_low_price',
            field=models.FloatField(default=100),
        ),
    ]
