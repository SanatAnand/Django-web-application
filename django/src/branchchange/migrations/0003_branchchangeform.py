# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0002_registerform'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchChangeForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('rollnumber', models.CharField(max_length=9, null=True, blank=True)),
                ('currentdept', models.CharField(max_length=100, null=True, blank=True)),
                ('cpi', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
    ]
