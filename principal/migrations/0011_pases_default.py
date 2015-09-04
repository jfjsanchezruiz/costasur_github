# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_auto_20141124_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='pases',
            name='default',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
