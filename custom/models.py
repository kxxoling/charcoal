# coding: utf-8
from django.db.models import CharField, ForeignKey, BooleanField, IntegerField, TextField
from django.db.models.signals import pre_save
from django.dispatch import receiver

from wagtail.wagtailimages.models import Image as _Image, Rendition as _Rendition
from wagtail.wagtailimages.models import AbstractImage, AbstractRendition

from .utils import auto_check_image


class SourcedImage(AbstractImage):

    class Meta:
        unique_together = (
            ('pixiv_id', 'pixiv_order'),
            ('da_username', 'da_path'),
        )

    orig_link = CharField(blank=True, null=True, max_length=300)
    source = CharField(blank=True, null=True, max_length=30)

    desc = TextField(blank=True, null=True)

    pixiv_id = IntegerField(null=True, default=None, blank=True)
    pixiv_order = IntegerField(null=True, default=0, blank=True)

    da_id = IntegerField(null=True, default=None, blank=True, unique=True)
    da_username = CharField(blank=True, null=True, default=None, max_length=50)
    da_path =  CharField(blank=True, null=True, default=None, max_length=150)

    is_restricted = BooleanField(null=False, default=False, blank=True)
    show = BooleanField(null=False, default=True, blank=True)

    admin_form_fields = _Image.admin_form_fields + (
        'orig_link',
        'pixiv_id',
        'pixiv_order',
        'da_id',
        'da_username',
        'da_path',
        'is_restricted',
        'show',
        'desc',
    )

    def get_pixiv_link(self):
        if not self.pixiv_id:
            return None
        return 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=%d' % self.pixiv_id


class ImageRendition(AbstractRendition):
    image = ForeignKey(SourcedImage, related_name='renditions')

    class Meta(_Rendition.Meta):
        unique_together = (('image', 'filter_spec', 'focal_point_key'), )


@receiver(pre_save, sender=SourcedImage)
def update_image(sender, instance, **kw):
    auto_check_image(instance)
