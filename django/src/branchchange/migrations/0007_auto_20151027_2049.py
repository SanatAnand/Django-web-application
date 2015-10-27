# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0006_auto_20151027_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchchangeform',
            name='category',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'GE'), (b'B', b'OBC'), (b'C', b'SC'), (b'D', b'ST')]),
        ),
        migrations.AlterField(
            model_name='branchchangeform',
            name='department',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Computer Science'), (b'B', b'Electrical Engineering'), (b'C', b'Mechanical Engineering'), (b'D', b'Civil Engineering')]),
        ),
    ]
