# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='gallery',
            field=models.ForeignKey(default=1, to='principal.Gallery'),
            preserve_default=False,
        ),
    ]
