# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 16:34
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_sharedlinkpage_videopage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='wagtailcore.Page'),
        ),
    ]