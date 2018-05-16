# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-08 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0010_auto_20180508_1210'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupacl',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='groupacl',
            name='component',
        ),
        migrations.RemoveField(
            model_name='groupacl',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='groupacl',
            name='language',
        ),
        migrations.RemoveField(
            model_name='groupacl',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='groupacl',
            name='project',
        ),
        migrations.DeleteModel(
            name='GroupACL',
        ),
    ]
