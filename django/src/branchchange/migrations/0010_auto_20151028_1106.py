# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0009_auto_20151028_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputstudentpreferrencelist',
            name='input_file',
            field=models.FileField(upload_to=b'/users/ug14/siddhant/Desktop/Branch_Change/django/src'),
        ),
    ]
