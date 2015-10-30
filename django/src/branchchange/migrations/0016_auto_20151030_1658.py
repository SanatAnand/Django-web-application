# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0015_auto_20151029_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchchangeform',
            name='category',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'GE'), (b'B', b'OBC'), (b'C', b'SC'), (b'D', b'ST'), (b'E', b'PwD')]),
        ),
        migrations.AlterField(
            model_name='branchchangeform',
            name='cpi',
            field=models.DecimalField(max_length=100, max_digits=4, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='branchchangeform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='branchchangeform',
            name='rollnumber',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
