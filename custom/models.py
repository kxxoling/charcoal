# coding: utf-8
from django.db.models import CharField, ForeignKey
from wagtail.wagtailimages.models import Image as _Image, Rendition as _Rendition
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition


class SourcedImage(AbstractImage):
    orig_link = CharField(blank=True, null=True, max_length=300)
    source = CharField(blank=True, null=True, max_length=30)

    admin_form_fields = _Image.admin_form_fields + (
        'orig_link',
    )


class ImageRendition(AbstractRendition):
    image = ForeignKey(SourcedImage, related_name='renditions')

    class Meta(_Rendition.Meta):
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

