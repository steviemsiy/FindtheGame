# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-06 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211206_0115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='playerprofile',
            options={'ordering': ['name']},
        ),
    ]
