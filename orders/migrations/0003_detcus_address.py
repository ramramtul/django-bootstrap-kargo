# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_detcus'),
    ]

    operations = [
        migrations.AddField(
            model_name='detcus',
            name='address',
            field=models.TextField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]