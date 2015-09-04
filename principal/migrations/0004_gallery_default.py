# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_gallery_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='default',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
