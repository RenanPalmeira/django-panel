# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_projectaccount_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=155)),
                ('content', models.TextField()),
                ('reference', models.CharField(max_length=155, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='ArticleConfiguration',
            fields=[
                ('id_article_configuration', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=155)),
                ('value', models.CharField(max_length=155)),
                ('icon', models.CharField(max_length=155, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
            options={
                'db_table': 'article_configuration',
            },
        ),
    ]
