# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0024_auto_20160305_1153'),
        ('question', '0005_auto_20160306_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Question_Set_From_Excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('excel_file', models.FileField(blank=True, null=True, upload_to='resource_files/')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Publishing Date: ')),
                ('edit_date', models.DateTimeField(blank=True, null=True, verbose_name='Editing Date: ')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa1.Question_Set')),
            ],
            options={
                'permissions': (('excel_upload', 'excel_upload'),),
            },
        ),
    ]
