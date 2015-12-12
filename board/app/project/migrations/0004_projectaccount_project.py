# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_projectaccount_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectaccount',
            name='project',
            field=models.ForeignKey(default='', to='project.Project'),
            preserve_default=False,
        ),
    ]
