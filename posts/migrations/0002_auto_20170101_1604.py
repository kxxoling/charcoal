# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='source',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
