# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([('last_name', 'first_name')]),
        ),
    ]