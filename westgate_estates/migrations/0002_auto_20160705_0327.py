# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general_enquiry',
            options={'verbose_name': 'Contact Form', 'verbose_name_plural': 'Contact Forms'},
        ),
        migrations.AlterModelOptions(
            name='property_enquiry',
            options={'verbose_name_plural': 'Property Enquiries'},
        ),
        migrations.AlterModelOptions(
            name='service_enquiry',
            options={'verbose_name_plural': 'Service Enquiries'},
        ),
        migrations.AddField(
            model_name='general_enquiry',
            name='replied_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='property_enquiry',
            name='replied_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='service_enquiry',
            name='replied_at',
            field=models.DateTimeField(null=True),
        ),
    ]
