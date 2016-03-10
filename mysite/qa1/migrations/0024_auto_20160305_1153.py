# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0023_auto_20160305_0652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcq_question',
            options={'verbose_name': ' Individual MCQ Questions '},
        ),
        migrations.AlterModelOptions(
            name='question_set',
            options={'verbose_name': 'Question Set'},
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='tag_inconsistent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='question_text',
            field=models.CharField(max_length=400),
        ),
    ]
