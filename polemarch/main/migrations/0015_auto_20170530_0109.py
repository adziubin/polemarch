# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-30 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_periodictask_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodictask',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='periodictask',
            name='project',
        ),
        migrations.RemoveField(
            model_name='typespermissions',
            name='periodic_tasks',
        ),
        migrations.DeleteModel(
            name='PeriodicTask',
        ),
    ]