# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=15, decimal_places=6)),
                ('ingredient_adjective', models.CharField(max_length=200, blank=True)),
                ('adjective_reverse', models.BooleanField(default=False)),
                ('ingredient_name', models.ForeignKey(to='recipes.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('add_date', models.DateField(default=datetime.date(2015, 1, 16), verbose_name=b'date added')),
                ('short_description', models.CharField(default=b'', max_length=120, blank=True)),
                ('details', models.TextField(default=b'')),
                ('line_items', models.ManyToManyField(to='recipes.LineItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('name_plural', models.CharField(max_length=25)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='unit',
            field=models.ForeignKey(to='recipes.Unit'),
            preserve_default=True,
        ),
    ]
