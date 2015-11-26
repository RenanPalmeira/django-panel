# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_applicationfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationfield',
            name='application',
        ),
        migrations.AddField(
            model_name='applicationfield',
            name='id_application',
            field=models.ForeignKey(db_column='id_application', default='', to='core.Application'),
            preserve_default=False,
        ),
    ]
