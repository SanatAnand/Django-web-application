# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0003_branchchangeform'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchchangeform',
            name='department',
            field=models.CharField(default=2, max_length=1, choices=[(b'CS', b'Computer Science'), (b'EE', b'Electrical Engineering'), (b'ME', b'Mechanical Engineering'), (b'CE', b'Civil Engineering')]),
            preserve_default=False,
        ),
    ]
