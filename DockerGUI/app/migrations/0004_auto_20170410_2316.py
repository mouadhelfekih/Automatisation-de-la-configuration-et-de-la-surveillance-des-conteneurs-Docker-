# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170410_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objet',
            old_name='iduser',
            new_name='id_user',
        ),
    ]
