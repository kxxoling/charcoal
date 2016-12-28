from __future__ import absolute_import, unicode_literals

from django.db.models import DateTimeField, CharField
from django.db.models import CASCADE, ForeignKey

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class PostTag(TaggedItemBase):
    content_object = ParentalKey('Post', related_name='tagged_posts')


class Post(Page):
    datetime_posted = DateTimeField('Post time', auto_now_add=True)
    datetime_edited = DateTimeField('Edit time', auto_now=True)
    intro = CharField(max_length=300)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=PostTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('tags'),
        ]),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    @property
    def tag_names(self):
        return self.tags.names()

    def get_context(self, request):
        context = super(Post, self).get_context(request)
        context['recent_posts'] = Post.objects.live()[:5]
        return context


class GalleryImage(Orderable):
    page = ParentalKey(Page, related_name='gallery_images')
    image = ForeignKey(
        'wagtailimages.Image', on_delete=CASCADE, related_name='+'
    )
    caption = CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
