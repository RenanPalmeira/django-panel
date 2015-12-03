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
            name='ProviderSocial',
            fields=[
                ('id_provider_social', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=155)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'social_provider',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id_social', models.AutoField(serialize=False, primary_key=True)),
                ('token', models.CharField(max_length=155)),
                ('username', models.CharField(max_length=155)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'social',
            },
        ),
    ]
