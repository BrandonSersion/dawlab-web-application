# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20180318_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('last_name',)},
        ),
    ]