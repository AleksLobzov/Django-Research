# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160204_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
    ]
