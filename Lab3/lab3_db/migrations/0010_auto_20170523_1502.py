# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_db', '0009_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='textbook',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
