# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170615_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='city',
            field=models.CharField(choices=[(' ', '---'), ('T', 'Toronto'), ('W', 'Windsor'), ('L', 'London')], default='---', max_length=20),
        ),
    ]