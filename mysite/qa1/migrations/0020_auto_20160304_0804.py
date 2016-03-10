# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0019_auto_20160304_0708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mcq_question',
            options={'verbose_name': 'All MCQ Questions List'},
        ),
        migrations.AlterModelOptions(
            name='question_set',
            options={'verbose_name': 'All Question Set List'},
        ),
        migrations.AlterModelOptions(
            name='question_topic',
            options={'verbose_name': 'Question Topic List'},
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='tag_content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='tag_sub_topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='tag_topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
