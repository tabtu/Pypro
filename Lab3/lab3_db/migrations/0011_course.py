# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_db', '0010_auto_20170523_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(to='lab3_db.Student')),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab3_db.Book')),
            ],
        ),
    ]