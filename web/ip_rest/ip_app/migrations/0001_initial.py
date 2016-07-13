# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='Ip address')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]