# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 03:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160523_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_body2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Body Of Post'),
        ),
    ]