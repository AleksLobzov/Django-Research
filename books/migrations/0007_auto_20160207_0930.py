# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160207_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]