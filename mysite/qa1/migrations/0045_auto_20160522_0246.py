# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0044_auto_20160522_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_set',
            name='reading_content',
            field=models.ManyToManyField(blank=True, null=True, to='readingmaterial.ReadingContent'),
        ),
        migrations.AlterField(
            model_name='question_set',
            name='special_plan',
            field=models.ManyToManyField(blank=True, null=True, to='subscription.Special_Plan'),
        ),
        migrations.AlterField(
            model_name='question_set',
            name='subscription_plan',
            field=models.ManyToManyField(blank=True, null=True, to='subscription.Subscription_Plan'),
        ),
    ]