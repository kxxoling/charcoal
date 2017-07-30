# coding: utf-8
from django.db.models import CharField, ForeignKey, BooleanField, IntegerField
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    show = BooleanField(null=False, default=True)

    admin_form_fields = _Image.admin_form_fields + (
        'orig_link', 'pixiv_id', 'pixiv_order', 'is_restricted', 'show',
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


@receiver(pre_save, sender=SourcedImage)
def update_image(sender, instance, **kw):
    # Set pixiv ID from link
    if instance.orig_link and instance.orig_link.startswith('https://www.pixiv.net/'):
        instance.pixiv_id = int(instance.orig_link.rsplit('=', 1)[-1])
    # Set link from pixiv ID
    if not instance.orig_link and instance.pixiv_id:
        instance.orig_link = instance.get_pixiv_link()
    # Clean file name
    instance.title = instance.title.strip('.jpg').strip('.png').strip('.gif').strip()

