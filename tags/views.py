# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from taggit.models import Tag


def show_tags(request):
    tag_list = Tag.objects.order_by('-id')
    paginator = Paginator(tag_list, 50)

    page = request.GET.get('page', 1)
    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)
    return render(request, 'tags/tags.html', {
        'tags': tags,
    })

