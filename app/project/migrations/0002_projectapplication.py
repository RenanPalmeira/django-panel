# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_application_order'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectApplication',
            fields=[
                ('id_project_application', models.AutoField(serialize=False, primary_key=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('application', models.ForeignKey(to='core.Application')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
                'db_table': 'project_application_set',
            },
        ),
    ]
