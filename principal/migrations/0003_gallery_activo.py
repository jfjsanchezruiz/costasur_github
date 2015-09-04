# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_items_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
