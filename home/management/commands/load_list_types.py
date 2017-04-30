# coding: utf-8
from django.core.management import BaseCommand
from home.models import list_page_models, HomePage


ArticleListPage, GalleryListPage, VideoListPage, SharedLinkListPage = list_page_models
list_pages = [
    dict(model=ArticleListPage, url='a', title='articles'),
    dict(model=GalleryListPage, url='g', title='galleries'),
    dict(model=VideoListPage, url='v', title='videos'),
    dict(model=SharedLinkListPage, url='l', title='links')
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        homepage = HomePage.objects.first()

        for p in list_pages:
            print p
            model = p['model']
            for i in model.objects.all():
                i.delete()
            page = model(title=p['title'], slug=p['url'], show_in_menus=True, depth=2)
            homepage.add_child(instance=page)
        print 'Pages successfully created!'
