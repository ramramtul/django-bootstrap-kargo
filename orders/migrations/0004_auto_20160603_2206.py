# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_detcus_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detcus',
            name='photo',
            field=models.ImageField(upload_to='uploads/customer'),
        ),
    ]