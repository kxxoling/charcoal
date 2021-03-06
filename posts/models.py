from __future__ import absolute_import, unicode_literals

from django.db.models import DateTimeField, CharField
from django.db.models import CASCADE, SET_NULL, ForeignKey

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from custom.models import SourcedImage as Image


class Tag(TaggedItemBase):
    content_object = ParentalKey('wagtailcore.Page', related_name='pages')


class BasePageModel(Page):

    class Meta:
        abstract = True

    datetime_posted = DateTimeField('Post time', auto_now_add=True)
    datetime_edited = DateTimeField('Edit time', auto_now=True)
    tags = ClusterTaggableManager(through=Tag, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('tags'),
        ]),
    ]

    def get_context(self, request):
        context = super(BasePageModel, self).get_context(request)
        context['recent_posts'] = Page.objects.type(
            (ArticlePage, GalleryPage, VideoPage, SharedLinkPage)
        ).live().order_by('-first_published_at')[:5]
        return context


class ArticlePage(BasePageModel):
    body = RichTextField(null=False)
    cover_image = ForeignKey(
        Image, related_name='articles', on_delete=SET_NULL, null=True, blank=True
    )

    search_fields = BasePageModel.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = BasePageModel.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('cover_image'),
    ]

    @property
    def tag_names(self):
        return self.tags.names()


class GalleryPage(BasePageModel):
    intro = RichTextField(null=True, blank=True)

    search_fields = BasePageModel.search_fields + [index.SearchField('intro')]

    content_panels = BasePageModel.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    @property
    def gallery_chunks(self, chunk_size=4):
        images = self.gallery_images.all()
        return [images[x:x + chunk_size] for x in range(0, len(images), chunk_size)]


class VideoPage(BasePageModel):
    link = CharField(max_length=300, null=False, blank=False)
    site = CharField(max_length=20, null=True, blank=True)

    content_panels = BasePageModel.content_panels + [
        FieldPanel('link'),
    ]


class SharedLinkPage(BasePageModel):
    link = CharField(max_length=300, null=False, blank=False)
    summary = CharField(max_length=300, null=False, blank=False)
    cover_image = ForeignKey(Image, related_name='+', on_delete=SET_NULL, null=True, blank=True)

    content_panels = BasePageModel.content_panels + [
        FieldPanel('link'),
        FieldPanel('summary'),
        ImageChooserPanel('cover_image'),
    ]


class GalleryImage(Orderable):
    page = ParentalKey(GalleryPage, related_name='gallery_images')
    image = ForeignKey('custom.SourcedImage', on_delete=CASCADE, related_name='+')
    caption = CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
