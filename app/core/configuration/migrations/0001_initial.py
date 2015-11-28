# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id_configuration', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'configuration',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id_permission', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
    ]
