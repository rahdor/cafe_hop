# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'')),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 50, 38, 724378))),
                ('cafe', models.ForeignKey(to='cafe_hop.Cafe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=5)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 50, 38, 724378))),
                ('cafe', models.ForeignKey(to='cafe_hop.Cafe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
