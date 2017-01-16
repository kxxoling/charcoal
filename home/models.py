from wagtail.wagtailcore.models import Page
from posts.models import ArticlePage, GalleryPage, VideoPage, SharedLinkPage


class HomePage(Page):

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['posts'] = Page.objects.type((ArticlePage, GalleryPage, VideoPage, SharedLinkPage)).live()
        context['recent_posts'] = Page.objects.type((
            ArticlePage, GalleryPage, VideoPage, SharedLinkPage)).live()
        return context
