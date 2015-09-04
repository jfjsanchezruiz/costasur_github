# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_items_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='orden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='nombre',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
