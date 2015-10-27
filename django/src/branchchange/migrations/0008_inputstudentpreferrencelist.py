# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0007_auto_20151027_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputStudentPreferrenceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
