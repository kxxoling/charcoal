from django.db import models
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from posts.models import ArticlePage


class ArticlesRSSFeed(Feed):
    title = "Articles"
    link = "/rss/a/"
    description = "All published articles."

    def items(self):
        return ArticlePage.objects.live().order_by('-first_published_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.url


class ArticlesAtomFeed(ArticlesRSSFeed):
    feed_type = Atom1Feed
    subtitle = ArticlesRSSFeed.description
    link = '/atom/a/'
