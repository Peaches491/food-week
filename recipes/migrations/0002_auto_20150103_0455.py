# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_name', models.CharField(max_length=200)),
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
                ('ingredient_adjective', models.CharField(max_length=200)),
                ('ingredient_name', models.ManyToManyField(to='recipes.Ingredient')),
                ('recipe', models.ManyToManyField(to='recipes.Recipe')),
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
        migrations.AlterField(
            model_name='recipe',
            name='add_date',
            field=models.DateField(verbose_name=b'date added'),
            preserve_default=True,
        ),
    ]
