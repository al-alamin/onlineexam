# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0011_auto_20160303_0826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtopic1',
            options={'verbose_name': 'Sub Topic Of Contents'},
        ),
        migrations.AddField(
            model_name='readingcontent',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Editing Date: '),
        ),
        migrations.AddField(
            model_name='readingcontent',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Publishing Date: '),
        ),
    ]