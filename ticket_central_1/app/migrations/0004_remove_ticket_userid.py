# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-10 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191208_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='userID',
        ),
    ]