# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20170316_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='../media/clients/'),
        ),
    ]