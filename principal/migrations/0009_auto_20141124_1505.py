# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20141120_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('langcode', models.CharField(max_length=10)),
                ('enurl', models.CharField(max_length=100)),
                ('esurl', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='items',
            name='tipo',
            field=models.CharField(default=b'I', max_length=1),
        ),
    ]
