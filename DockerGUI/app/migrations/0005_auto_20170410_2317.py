# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170410_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objet',
            old_name='id_user',
            new_name='username',
        ),
    ]
