# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcedimage',
            name='is_restricted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sourcedimage',
            name='pixiv_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='sourcedimage',
            name='pixiv_order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='sourcedimage',
            unique_together=set([('pixiv_id', 'pixiv_order')]),
        ),
    ]