# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-10 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ticket_ticket_fix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='Active', help_text='Please enter Active, Resolved or In-progress', max_length=25),
        ),
    ]
