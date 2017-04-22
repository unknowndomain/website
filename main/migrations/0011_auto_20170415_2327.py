# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_space_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='country',
            field=models.CharField(choices=[('ENGLAND', 'England'), ('GUERNSEY', 'Guernsey'), ('IRELAND', 'Ireland'), ('SCOTLAND', 'Scotland'), ('WALES', 'Wales')], default='ENGLAND', max_length=50),
        ),
    ]
