# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170307_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barber',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='barber',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
