# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160207_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='logo',
            field=models.ImageField(null=True, upload_to='/tmp'),
        ),
    ]
