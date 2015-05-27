# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_hop', '0002_auto_20150526_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 3, 22, 13, 886095)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 3, 22, 13, 886095)),
            preserve_default=True,
        ),
    ]
