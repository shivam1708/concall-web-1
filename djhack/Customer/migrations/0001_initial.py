# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-10 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('cuid', models.IntegerField(default=1, unique=True)),
                ('total_issues', models.IntegerField(default=0)),
            ],
        ),
    ]
