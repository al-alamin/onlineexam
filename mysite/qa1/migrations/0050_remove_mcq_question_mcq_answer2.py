# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0049_question_set_result_can_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcq_question',
            name='mcq_answer2',
        ),
    ]
