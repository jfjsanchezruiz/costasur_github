# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20141124_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pases',
            name='enurl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='pases',
            name='esurl',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
