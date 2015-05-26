# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_hop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 1, 0, 5, 699273)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 1, 0, 5, 699273)),
            preserve_default=True,
        ),
    ]
