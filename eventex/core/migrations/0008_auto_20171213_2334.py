# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 23:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]
