# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20141120_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='orden',
            field=models.IntegerField(unique=True),
        ),
    ]
