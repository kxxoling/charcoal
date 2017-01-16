from wagtail.wagtailcore.models import Page
from posts.models import ArticlePage


class HomePage(Page):

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['posts'] = ArticlePage.objects.live()
        context['recent_posts'] = ArticlePage.objects.live()
        return context
