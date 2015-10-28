# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0010_auto_20151028_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputBranchList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_file', models.FileField(upload_to=b'/users/ug14/siddhant/Desktop/Branch_Change/django/src')),
            ],
        ),
    ]
