# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20170317_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profilePic',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]