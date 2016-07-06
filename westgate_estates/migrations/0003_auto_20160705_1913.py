# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0002_auto_20160705_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='general_enquiry',
            name='conversation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property_enquiry',
            name='conversation',
            field=models.TextField(default=b'Not yet replied'),
        ),
        migrations.AddField(
            model_name='service_enquiry',
            name='conversation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
