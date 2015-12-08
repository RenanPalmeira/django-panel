# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectaccount',
            name='project',
        ),
    ]
