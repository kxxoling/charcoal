# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.wagtailimages import get_image_model


Image = get_image_model()


def show_images(request):
    image_list = Image.objects.order_by('-id')
    paginator = Paginator(image_list, 24)

    page = request.GET.get('page', 1)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'images/images.html', {
        'images': images,
    })

