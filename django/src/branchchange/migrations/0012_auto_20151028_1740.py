# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0011_inputbranchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputbranchlist',
            name='input_file',
            field=models.FileField(upload_to=b'/home/ritwick/Branch_Change/django/src'),
        ),
        migrations.AlterField(
            model_name='inputstudentpreferrencelist',
            name='input_file',
            field=models.FileField(upload_to=b'/home/ritwick/Branch_Change/django/src'),
        ),
    ]
