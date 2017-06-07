# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from taggit.models import Tag

from wagtail.wagtailimages import get_image_model


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


def show_tagged_figures(request, tag_id_in_str):
    tag_id = int(tag_id_in_str)
    tag = get_object_or_404(Tag, pk=tag_id)
    Image = get_image_model()
    figures = Image.objects.filter(tags__id=tag_id)
    return render(request, 'tags/tagged_figures.html', {
        'tag': tag,
        'figures': figures,
    })

