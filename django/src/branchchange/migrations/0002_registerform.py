# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branchchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100, null=True, blank=True)),
                ('password', models.CharField(max_length=100, null=True, blank=True)),
                ('confirmpassword', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
