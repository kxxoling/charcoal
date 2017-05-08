from wagtail.wagtailcore.models import Page
from posts.models import ArticlePage, GalleryPage, VideoPage, SharedLinkPage


PAGE_TYPES = (ArticlePage, GalleryPage, VideoPage, SharedLinkPage,)


class BaseIndexPage(Page):
    _page_types = ()

    class Meta:
        abstract = True

    def get_context(self, request):
        context = super(BaseIndexPage, self).get_context(request)
        context['recent_posts'] = Page.objects.type(PAGE_TYPES).live()
        context['posts'] = Page.objects.type(self._page_types).live()
        return context

    def get_template(self, request):
        return 'home/home_page.html'


def gen_list_page(model, app_label='', module='home'):
    name = model.__name__.replace('Page', 'ListPage')

    class Meta:
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Set up a dictionary to simulate declarations within a class
    attrs = {
        '__module__': module,
        'Meta': Meta,
        '_page_types': (model,),
        'subpage_types': (model,),
    }

    return type(name, (BaseIndexPage,), attrs)


list_page_models = map(gen_list_page, PAGE_TYPES)      # (ArticleListPage, VideoListPage, GalleryListPage, SharedLinkListPage)


class HomePage(BaseIndexPage):
    _page_types = PAGE_TYPES
    subpage_types = list_page_models

