# coding: utf-8
from django.db.models import CharField, ForeignKey, BooleanField, IntegerField
from wagtail.wagtailimages.models import Image as _Image, Rendition as _Rendition
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition


class SourcedImage(AbstractImage):
    class Meta:
        unique_together = ('pixiv_id', 'pixiv_order')

    orig_link = CharField(blank=True, null=True, max_length=300)
    source = CharField(blank=True, null=True, max_length=30)

    pixiv_id = IntegerField(null=True, default=None, blank=True)
    pixiv_order = IntegerField(null=True, default=0, blank=True)

    is_restricted = BooleanField(null=False, default=False)

    admin_form_fields = _Image.admin_form_fields + (
        'orig_link', 'pixiv_id', 'pixiv_order', 'is_restricted',
    )

    def get_pixiv_link(self):
        if not self.pixiv_id:
            return None
        return 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=%d' % self.pixiv_id


class ImageRendition(AbstractRendition):
    image = ForeignKey(SourcedImage, related_name='renditions')

    class Meta(_Rendition.Meta):
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

