# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_hop', '0003_auto_20150527_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 12, 26, 867977)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 12, 26, 867977)),
            preserve_default=True,
        ),
    ]
