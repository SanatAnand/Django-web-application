# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0005_auto_20151027_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branchchangeform',
            name='currentdept',
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='category',
            field=models.CharField(default=b'GE', max_length=1, choices=[(b'GE', b'GE'), (b'OBC', b'OBC'), (b'SC', b'SC'), (b'ST', b'ST')]),
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='pref1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='pref2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='pref3',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='pref4',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='branchchangeform',
            name='pref5',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='branchchangeform',
            name='cpi',
            field=models.DecimalField(max_length=100, max_digits=4, decimal_places=2),
        ),
    ]
