# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0008_inputstudentpreferrencelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputstudentpreferrencelist',
            name='input_file',
            field=models.FileField(upload_to=b'/home/ritwick/Branch_Change/django/src'),
        ),
    ]
