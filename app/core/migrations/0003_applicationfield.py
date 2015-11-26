# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_application_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationField',
            fields=[
                ('id_application_field', models.AutoField(serialize=False, primary_key=True)),
                ('field', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('order', models.SmallIntegerField(null=True)),
                ('required', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('application', models.ForeignKey(to='core.Application')),
            ],
            options={
                'db_table': 'application_field',
            },
        ),
    ]
