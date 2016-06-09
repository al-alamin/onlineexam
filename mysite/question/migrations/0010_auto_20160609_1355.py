# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0034_auto_20160603_2032'),
        ('question', '0009_auto_20160608_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Quick_Question_From_Excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='resource_files/quickquestion/')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Publishing Date: ')),
                ('edit_date', models.DateTimeField(blank=True, null=True, verbose_name='Editing Date: ')),
                ('reading_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.ReadingContent')),
            ],
            options={
                'permissions': (('excel_question_set_upload', 'excel_question_set_upload'),),
            },
        ),
        migrations.AlterField(
            model_name='upload_question_set_from_excel',
            name='excel_file',
            field=models.FileField(upload_to='resource_files/mcq/'),
        ),
    ]
