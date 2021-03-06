# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170116_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='source',
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='custom.SourcedImage'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='custom.SourcedImage'),
        ),
        migrations.AlterField(
            model_name='sharedlinkpage',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='custom.SourcedImage'),
        ),
    ]
