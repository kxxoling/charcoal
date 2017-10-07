# coding: utf-8
from django.conf import settings


def template_env(request):
    return {
        'SITE_TITLE': settings.SITE_TITLE,
    }
