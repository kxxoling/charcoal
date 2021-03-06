# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
        ('posts', '0004_auto_20170116_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedLinkPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('datetime_posted', models.DateTimeField(auto_now_add=True, verbose_name='Post time')),
                ('datetime_edited', models.DateTimeField(auto_now=True, verbose_name='Edit time')),
                ('link', models.CharField(max_length=300)),
                ('summary', models.CharField(max_length=300)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='posts.Tag', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='VideoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('datetime_posted', models.DateTimeField(auto_now_add=True, verbose_name='Post time')),
                ('datetime_edited', models.DateTimeField(auto_now=True, verbose_name='Edit time')),
                ('link', models.CharField(max_length=300)),
                ('site', models.CharField(blank=True, max_length=20, null=True)),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='posts.Tag', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
