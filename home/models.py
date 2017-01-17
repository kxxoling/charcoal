from wagtail.wagtailcore.models import Page
from posts.models import ArticlePage, GalleryPage, VideoPage, SharedLinkPage


PAGE_TYPES = (ArticlePage, GalleryPage, VideoPage, SharedLinkPage,)


class HomePage(Page):
    subpage_types = list(PAGE_TYPES)

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['posts'] = Page.objects.type(PAGE_TYPES).live()
        context['recent_posts'] = Page.objects.type(PAGE_TYPES).live()
        return context
