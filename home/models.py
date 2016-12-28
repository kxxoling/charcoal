from wagtail.wagtailcore.models import Page
from posts.models import Post


class HomePage(Page):

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['posts'] = Post.objects.live()
        context['recent_posts'] = Post.objects.live()
        return context
